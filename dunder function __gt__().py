#!/bin/python3

#creating a class Order that stores items and its price
# usign dunder function __gt__()
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
        
odr1 = Order("Ice-Cream", 55)
odr2 = Order("Biscuits", 120)

print("Print True or False:", odr1 > odr2)


    
