#!/bin/python3

class Account:
    def __init__(self, acc_no, acc_pass):
        #if we add two underscore before any variable it becomes private variable.
        #e.g: self.acc_no is public but self.__acc_no is private variable
        self.__acc_no = acc_no
        self.__acc_pass = acc_pass

    def __reset_pass(self):
        #if we add two under score before any methods it becomes private methods.
        #only member function of a class can access private variables.
        print(self.__acc_no)
        print(self.__acc_pass)
    
    def display(self):
        #calling private method __reset_pass()
        self.__reset_pass()
        

#creating object of class Account
acc1 = Account(1307787343, "ABXYZ!!@@##")

#we can't access private variables from outside of class
#print(acc1.__acc_no)
#print(acc1.__acc_pass)

#we can access private variables and methods using member functions of that class
acc1.display()