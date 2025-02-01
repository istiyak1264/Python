#!/bin/python3

class Car:
    def __init__(self):
        self.acclerator = False
        self.brake = False
        self.clutch = False

    def start(self):
        #here self.acclerator and self.clutch become true in the background
        #user can't see the implementation. This is called Abstraction. 
        self.acclerator = True
        self.clutch = True
        print("car started...")

#creating object of class Car
car1 = Car()
car1.start()