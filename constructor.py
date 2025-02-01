#!/bin/python3

class Student:
    #below constructor is default constructor.
    def __init__(self):
        pass
    #here __init__(self) is the constructor and it takes self as argument.
    #we can write anything at the place of self.
    #below constructor is parameterized constructor.
    def __init__(self, name, marks):
        #if we print(self), it will print s1 object's memory address.
        #it means self stores object's memory address.
        print("print(self):", self)
        self.name = name
        self.marks = marks

s1 = Student("Istiyak Ahmed", 88)

#here s1 is the object of class Student.
#if we print s1, it will print memory address of s1.
print("print(s1):", s1)
print("Name :", s1.name)
print("Marks:", s1.marks)

s2 = Student("Ahmed Imran", 97)
print("Name :", s2.name)
print("Marks:", s2.marks)