#!/bin/python3
def print_natural_number(n):
    if(n==0):
        return
    print_natural_number(n-1)
    print(n)
    
#taking input from user and calling function:
n = int(input("Enter the number: "))
print_natural_number(n)
