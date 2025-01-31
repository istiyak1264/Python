#!/bin/python3
file = open("w+Mode.txt", "w+")
#when we open file in w+ mode it will delete all the exitsting data of the file first.
#At this point the file will be empty.
#Then the data will be written in the file.
file.write("A quick brown fox jumps over the lazy dogs.")

#below line will show the file empty because the file pointer moves ends of the file
print(file.read())
file.close()
#After closing the file if we open the file in reading mode we can see the new data.
#Because now file pointer has moved to the beginning.

file = open("w+Mode.txt", "r")
print(file.read())
file.close()