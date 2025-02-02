#!/bin/python3

class complex:
    #if we add two underscore before a function name it is called Dunder function
    def __init__(self, real, img):
        self.real = real
        self.img = img

    #adding two complex numbers using operator overloading
    def __add__(self, num2):
        NewReal = self.real + num2.real
        NewImg = self.img + num2.img
        return complex(NewReal, NewImg)
    
    #substracting a complex number from another
    def __sub__(self, num2):
        NewReal = self.real - num2.real
        NewImg = self.img - num2.img
        return complex(NewReal, NewImg)

    def display(self):
        if self.img >= 0:
            print(self.real, "+", self.img, "i")
        else:
            print(self.real, "-", abs(self.img), "i")

#creating object of class complex
num1 = complex(1, 3)
num1.display()

num2 = complex(4, 5)
num2.display()

#operator overloading of "+" operator
num3 = num1 + num2
num3.display()

#operator overloading of "-" operator
num3 = num1 - num2
num3.display()