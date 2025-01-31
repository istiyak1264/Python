#!/bin/python3
str1 = input("Enter str1: ")
str2 = input("Enter str2: ")

#printing the length of str1 using len(string_name)
print("Length of str1:",len(str1))

#printing the length of str2 using len(string_name)
print("Length of str2:",len(str2))

#concatenation of two strings.
final_str = str1 + " " + str2

#printing the concatenated string
print("Concatenation of strings:", final_str)

#Below line will print data from index1 to index 10 of final_str
print(final_str[1:10])

#Below line will print data from starting to index 5.
print(final_str[:5])

#Below line will print data from index 3 to end of the string
print(final_str[3:])

#Below line will print data from index 2 to end of the string
print(final_str[2:len(final_str)])

