#!/bin/python
str = input("Enter traffic light color: ")
if(str == "red"):
    print("STOP")
elif(str == "yellow"):
    print("LOOK")
elif(str == "green"):
    print("GO")
else:
    print("Invalid Input.")