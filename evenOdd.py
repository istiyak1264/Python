#!/bin/python

a = int(input("Enter a number: "))
if(a == 0):
    print("Entered number is Zero.")
elif(a % 2 == 0):
    print(a, "is an even number")
else:
    print(a, "is an odd number")
