#!/bin/python3

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    #this is called property decorator
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

    def display(self):
        print(self.percentage)
        
#creating object of class Student
s1 = Student(98, 95, 97)
s1.display()

s1.phy = 85
s1.display()