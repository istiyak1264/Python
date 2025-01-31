#!/bin/python3
import os
#with syntax is another useful concept for opening file.
with open("demo.txt", "w") as f:
    f.write("A quick brown fox jumps over the lazy dogs.")
#if we open file using with syntax we don't need to close file manually
#with syntax will close file automatically implicitly.

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)

#below line is used to delete a file.
# Here os is a module in python. Module is like a code library that has inbuilt functions.
os.remove("demo.txt")