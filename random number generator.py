#!/bin/python3
import random

#generating random number using random function()
target = random.randint(1, 100)
while True:
    UserChoice = input("Guess the Target or Quit(Q): ")
    if(UserChoice == "Q"):
        break
    #converting UserChoice from string to integer
    UserChoice = int(UserChoice)

    #checkig the conditions
    if(target == UserChoice):
        print("Success: Correct Guess!!")
        break
    
    elif(UserChoice < target):
        print("Your number was too small. Guess a little bit bigger number...")
    
    else:
        print("Your number was too big. Guess a little bit smaller number...")

#when user successfully guess the number the game is over.
print("-----------Game Over----------")