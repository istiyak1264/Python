#!/bin/python3

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = n * factorial(n - 1)
    print("Factorial of", n, ":", result)
    return result

# Taking input and function call
n = int(input("Enter the number: "))
factorial(n)
