#!/bin/python3
import random
import string

#password length is 12
password_length = 12

#taking a list of all possible characters to generate strong random password.
charValues = string.ascii_letters + string.digits + string.punctuation
print(charValues)


#list comprehension [function for i in range(n)]
Password = "".join([random.choice(charValues) for i in range(password_length)])
print("Lis comprehension Password is: ", Password)

#taking an empty string to save 12 random characters.
password = ""

#generating 12 random characters.
for i in range(password_length):
    password += random.choice(charValues)

#printing the randomly generated password.
print("Randomly generated password is:", password)