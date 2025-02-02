#!/bin/python3
import random

target = random.randint(1, 100)
while True:
    UserChoice = int(input("Guess the Target: "))
    if(target == UserChoice):
        print("Success: Correct Guess!!")
        break
    
    elif(UserChoice < target):
        print("Your number was too small. Guess a little bit bigger number...")
    
    else:
        print("Your number was too big. Guess a little bit smaller number...")

print("-----------Game Over----------")