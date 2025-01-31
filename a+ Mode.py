#!/bin/python3

#opening file in the append mode.
#append means add at the end.
file = open("a+Mode.txt", "a+")
#a+ mode means opening file in read and append mode.

#below line will not delete the existing data.
#Instead below data will be written at the end of existing data of the file.
file.write("A quick brown fox jumps over the lazy dogs.")

#below line will print empty lines. because file pointer has moved to the last of the file
print(file.read())
#below line is closing the file in a+ mode
file.close()

#after closing the file if we open the file in reading mode we can read the full data of the file.
file = open("a+Mode.txt", "r")
print(file.read())

#below line is closing the file in reading mode
file.close()