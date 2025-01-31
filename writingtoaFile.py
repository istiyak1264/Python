#!/bin/python3

#opening file in writing mode
f = open("example.txt", "w")

#f.write() function will overwrite the full file
# It means it will delete exitsting data and save the below data.
f.write("Hi, I am Istiyak Ahmed and I am learning Python.")
#closing writing mode of the file
f.close()

#opening the file in reading mode
f = open("example.txt", "r")

#printing the file data
print(f.read())

#closing reading mode of the file
f.close()


