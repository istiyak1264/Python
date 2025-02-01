#!/bin/python3

class base1:
    var1 =("Welcome to class base1.")

class base2:
    var2 =("Welcome to class base2.")

class child(base1, base2):
    var3 =("Welcome to class base3.")


#creating objects of class child.
obj1 = child()
print(obj1.var1)
print(obj1.var2)
print(obj1.var3)