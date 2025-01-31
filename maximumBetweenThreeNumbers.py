#!/bin/python3
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if(a>b and a>c):
    print("a is maximum.")
elif(b>c):
    print("b is maximum.")
elif(a==b and b==c):
    print("a, b and c are equal.")
else:
    print("c is maximum")