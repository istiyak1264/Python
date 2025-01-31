#!/bin/python3
range = int(input("Enter the number printing range: "))
i = 1
while i <= range:
    print(i) if i%2 != 0 else None
    i+=1