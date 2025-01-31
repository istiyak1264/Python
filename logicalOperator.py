#!/bin/python
mark = int(input("Enter the marks: "))
if(mark >= 80):
    print("A+")
elif(mark >= 75 and mark < 80):
    print("A")
elif(mark >= 70 and mark < 75):
    print("A-")
elif(mark >= 65 and mark < 70):
    print("B+")
elif(mark >= 60 and mark < 65):
    print("B-")
elif(mark >= 55 and mark < 60):
    print("C")
elif(mark >= 50 and mark < 55):
    print("D")
elif(mark >= 45 and mark < 50):
    print("E")
else:
    print("Failed")