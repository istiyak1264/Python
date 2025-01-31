#!/bin/python3

#tuple is a builtin data-type that let us create immutable sequence of values
tup = (3, 1, 5, 3, 7, 11, 9, 7, 3, 17)
print(type(tup))

#tup[0] = 5 or change of any index's value is not allowed in tuple.
#this is the main difference between tuple and list. But othe thing works like lists in tuple
print(tup[0])
print(tup[1:5])

#tup.index(element) returns the first occurance index no of the element.
print(tup.index(3))

#tup.count(element) returns the total occurances of the element
print(tup.count(3))