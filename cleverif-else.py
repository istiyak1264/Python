#!/bin/python3

#clever if-else syntax: <variable_name> = (false_value, true_value) [condition]
age = int(input("Enter your age:"))
vote = ("No", "Yes") [age >= 18]
print(vote)