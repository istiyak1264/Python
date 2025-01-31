#!/bin/python3

#opening sample.txt file in reading mode
f = open("sample.txt", "r")

#reading items from the file and saving it to a variable named data
data = f.read()
print(data)

# Reset file pointer to the beginning
f.seek(0)

#reading 10 characters from the whole file
data = f.read(10)
print(data)

# Reset file pointer to the beginning
f.seek(0)

#printing single line at a time
line1 = f.readline()
print(line1)
#after first line it will show a empty line. this is because "\n"

line2 = f.readline()
print(line2)

#closing the file
f.close()
