#!/bin/python3

class Student:
    #__init__(self) is default constructor.
    def __init__(self):
        pass

    #__init__(self, name, marks) is parameterized constructor.
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    #this is a method
    def get_name(self):
        #self stores the memory address of the object
        return self.name

    def get_marks(self):
        return self.marks
    
    #static method don't take (self) reference as parameter
    @staticmethod
    def Greeting():
        print("Hi, I am", s1.name, "and I am learning Python.")

#creating objects of Student class
s1 = Student("Istiyak Ahmed", 97)

#calling get_name() and get_marks() method.
print("Name:", s1.get_name())
print("Marks:", s1.get_marks())
s1.Greeting()