#!/bin/python3

class Car:
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped...")

# ToyotaCar is the child class of Car.
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

# Fortuner is the child class of ToyotaCar.
class Fortuner(ToyotaCar):
    def __init__(self, name, brand):  # Added 'name' parameter to inherit properly from ToyotaCar
        super().__init__(name)  # Call the parent constructor
        super().start()
        super().stop()
        self.brand = brand

# Creating objects of class Fortuner
car1 = Fortuner("Fortuner", "Rolls Royce Ghost")  # Corrected class instantiation
car2 = Fortuner("Fortuner", "Bugatti Chiron")  # Corrected class instantiation

print(car1.name)  # This works correctly
print(car1.brand)  # Print brand instead of incorrect name access
car1.start()  # Removed print() since start() already prints output
car1.stop()

print(car2.name)  # This works correctly
print(car2.brand)  # Print brand instead of incorrect name access
car2.start()
car2.stop()
