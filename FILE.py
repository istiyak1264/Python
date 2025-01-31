#!/bin/python3

#opening a file in reading mode
f = open("sample.txt", "r")
data = f.read()
print(data)
f.close()