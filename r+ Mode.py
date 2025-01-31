#!/bin/python3

#opening the file in reading writing mode.
f = open("r+Mode.txt", "r+")

#below line will overwrite the file from staring.
f.write("A quick brown fox")

#below line will print the existing data that hasn't been overwritten yet.
print(f.read())
f.close()

#After closing when we open the file in r+ mode again it will print the whole updated data of the file.
f = open("r+Mode.txt", "r+")
print(f.read())

#e.g: existing data in r+Mode.txt file: Hi, I am Istiyak Ahmed and I am learning Python.
#after writing "A quick brown fox" the new data in r+Mode.txt file:
#A quick brown foxAhmed and I am learning Python.
#r+ mode has overwritten the "A quick brown fox" equal characters in the exting data of the file
