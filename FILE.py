#!/bin/python3

# Opening a file in reading mode
f = open("sample.txt", "r")

# Reading the full file
data = f.read()
print(data)

# Moving the cursor back to the beginning before reading again
f.seek(0)

# Reading only 10 characters from the file
data = f.read(10)
print(data)

# Reading one line at a time
data = f.readline()
print(data)

# Closing the file
f.close()