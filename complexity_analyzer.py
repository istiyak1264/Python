import re
import sys
from collections import defaultdict

class ComplexityAnalyzer:
    def __init__(self):
        self.patterns = {
            'O(1)': [
                r'\b(?:print|printf|cout|System\.out\.println|console\.log)\b',
                r'\b(?:assignment|return|break|continue)\b',
                r'\b(?:math|arithmetic|comparison)\b'
            ],
            'O(log n)': [
                r'\b(?:divide\s*and\s*conquer|binary\s*search|tree\s*traversal)\b',
                r'\b(?:while|for)\s*\(.*?\/=.*?\)',
                r'\b(?:while|for)\s*\(.*?\b(?:n\s*=\s*n\s*\/\s*\d+|n\s*\/=\s*\d+)\b'
            ],
            'O(n)': [
                r'\b(?:for|while)\s*\(.*?\b(?:i\s*[<>]=?\s*n|i\s*[<>]=?\s*len|i\s*[<>]=?\s*array\.length)\b',
                r'\b(?:for|while)\s*\(.*?\b(?:i\s*<\s*[a-zA-Z_][a-zA-Z0-9_]*\.length|size|count)\b',
                r'\b(?:for|foreach)\s*\(.*?\b(?:in|:)\b'
            ],
            'O(n log n)': [
                r'\b(?:merge\s*sort|quick\s*sort|heap\s*sort)\b',
                r'\b(?:divide\s*and\s*conquer)\b.*?\b(?:linear\s*work)\b',
                r'\b(?:for\s*\(.*?\).*?\{.*?\b(?:log\s*n\b).*?\})'
            ],
            'O(n²)': [
                r'\b(?:for\s*\(.*?\).*?\{.*?\bfor\s*\(.*?\).*?\})',
                r'\b(?:nested\s*loops)\b',
                r'\b(?:bubble\s*sort|selection\s*sort|insertion\s*sort)\b',
                r'\b(?:matrix\s*multiplication)\b'
            ],
            'O(n³)': [
                r'\b(?:for\s*\(.*?\).*?\{.*?\bfor\s*\(.*?\).*?\{.*?\bfor\s*\(.*?\).*?\}\s*\})',
                r'\b(?:three\s*nested\s*loops)\b'
            ],
            'O(2^n)': [
                r'\b(?:recursion)\b.*?\b(?:multiple\s*calls)\b',
                r'\b(?:brute\s*force)\b',
                r'\b(?:fibonacci\s*without\s*memoization)\b',
                r'\b(?:power\s*set|subsets|combinations)\b'
            ],
            'O(n!)': [
                r'\b(?:permutations|traveling\s*salesman|brute\s*force\s*search)\b',
                r'\b(?:generate\s*all\s*possible)\b'
            ]
        }
        
        self.recursion_keywords = [
            r'\b(?:function|def|fun|method)\b.*?\b(?:calls\s*itself|recursion)\b',
            r'\b(?:return\s.*?\b(?:same\s*function|self))\b',
            r'\b(?:function|def|fun|method)\b.*?\{.*?\b(?:function|def|fun|method)\b.*?\}'
        ]
        
        self.loop_patterns = [
            r'\b(?:for|while|do\s*while|foreach)\s*\(?.*?\)?\s*\{?',
            r'\b(?:for|while|do\s*while|foreach)\s*.*?\b(?:in|:)\b'
        ]
        
        self.sorting_algorithms = {
            'bubble sort': r'\b(?:bubble\s*sort)\b',
            'merge sort': r'\b(?:merge\s*sort)\b',
            'quick sort': r'\b(?:quick\s*sort)\b',
            'selection sort': r'\b(?:selection\s*sort)\b',
            'insertion sort': r'\b(?:insertion\s*sort)\b'
        }

    def analyze_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                code = file.readlines()
                return self.analyze_code(code)
        except FileNotFoundError:
            return {"error": "File not found"}
        except Exception as e:
            return {"error": str(e)}

    def analyze_code(self, code_lines):
        complexity_counts = defaultdict(int)
        has_recursion = False
        loop_depth = 0
        max_loop_depth = 0
        detected_algorithm = None
        
        # Check for recursion and known algorithms
        for line in code_lines:
            line = line.strip()
            if not line or line.startswith(('//', '/*', '*', '*/', '#', '--')):
                continue
                
            for pattern in self.recursion_keywords:
                if re.search(pattern, line, re.IGNORECASE):
                    has_recursion = True
                    break
                    
            for algo, pattern in self.sorting_algorithms.items():
                if re.search(pattern, line, re.IGNORECASE):
                    detected_algorithm = algo
                    break
        
        # Count loop patterns and nested levels
        for line in code_lines:
            line = line.strip()
            if not line or line.startswith(('//', '/*', '*', '*/', '#', '--')):
                continue
                
            loop_start = False
            for pattern in self.loop_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    loop_start = True
                    break
                    
            if loop_start:
                loop_depth += 1
                max_loop_depth = max(max_loop_depth, loop_depth)
            elif '}' in line or 'end' in line or 'fi' in line or 'done' in line:
                loop_depth = max(0, loop_depth - 1)
        
        # Check for complexity patterns
        for complexity_type, patterns in self.patterns.items():
            for pattern in patterns:
                for line in code_lines:
                    line = line.strip()
                    if not line or line.startswith(('//', '/*', '*', '*/', '#', '--')):
                        continue
                        
                    if re.search(pattern, line, re.IGNORECASE):
                        complexity_counts[complexity_type] += 1
        
        # Determine the most likely complexity
        if detected_algorithm:
            if 'bubble' in detected_algorithm or 'selection' in detected_algorithm or 'insertion' in detected_algorithm:
                most_likely = 'O(n²)'
            elif 'merge' in detected_algorithm or 'quick' in detected_algorithm or 'heap' in detected_algorithm:
                most_likely = 'O(n log n)'
        elif complexity_counts:
            most_likely = max(complexity_counts.items(), key=lambda x: x[1])[0]
        else:
            most_likely = 'O(1)'
        
        # Adjust based on loop depth
        if max_loop_depth >= 3:
            most_likely = 'O(n³)' if max_loop_depth == 3 else f'O(n^{max_loop_depth})'
        elif max_loop_depth == 2 and most_likely in ['O(n)', 'O(n²)']:
            most_likely = 'O(n²)'
        elif max_loop_depth == 1 and most_likely == 'O(n)':
            most_likely = 'O(n)'
        
        # Adjust based on recursion
        if has_recursion:
            if most_likely in ['O(1)', 'O(n)']:
                most_likely = 'O(2^n)'
            elif most_likely == 'O(log n)':
                most_likely = 'O(n log n)'
        
        # Generate report
        report = {
            'time_complexity': most_likely,
            'complexity_indicators': dict(complexity_counts),
            'has_recursion': has_recursion,
            'max_loop_depth': max_loop_depth,
            'detected_algorithm': detected_algorithm
        }
        
        return report

def print_report(report):
    if isinstance(report, str):
        print(report)
        return
    
    if 'error' in report:
        print(f"Error: {report['error']}")
        return
    
    print("\n=== Code Complexity Analysis Report ===")
    print(f"Estimated time complexity: {report['time_complexity']}")
    
    if report['detected_algorithm']:
        print(f"\nDetected algorithm: {report['detected_algorithm']}")
    
    if report['complexity_indicators']:
        print("\nComplexity indicators found:")
        for comp, count in report['complexity_indicators'].items():
            print(f"[+] {comp}: {count} occurrences")
    
    print("\nAdditional findings:")
    print(f"[+] Recursion: {'Yes' if report['has_recursion'] else 'No'}")
    print(f"[+] Maximum loop nesting depth: {report['max_loop_depth']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python complexity_analyzer.py <filename>")
        return
    
    filename = sys.argv[1]
    analyzer = ComplexityAnalyzer()
    report = analyzer.analyze_file(filename)
    print_report(report)

if __name__ == "__main__":
    main()

