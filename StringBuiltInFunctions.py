#!/bin/python3
str = "hi, I am Istiyak Ahmed and I am learning Python"

"""str.endswith("Python") function will chech if the string ends with Python or not.
if the string ends with "Python" it will print true otherwise false"""
print(str.endswith("Python"))


#str.capitalize() will capitalize the first character of the string str.
print(str.capitalize())

#str.replace(old_value, new_value) replaces the portion of a string with new value
print(str.replace("Istiyak", "Imran"))

#str.find("str") will print the index no of first character of the string str.
print(str.find("Istiyak Ahmed"))

#str.count("sub_str") will print the occurance of the substr.
print(str.count("am"))