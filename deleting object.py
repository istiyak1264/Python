#!/bin/python3

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student("Istiyak Ahmed", 230103)

print(s1)
print(s1.name)
#below line will delete the object s1

#it will delete the object name
del s1.name
print(s1.name) #it will throw error

#it will delete the entire object
del s1
print(s1) #it will throw error