#!/bin/python3

student = {
    "name" : "Istiyak Ahmed",
    #here subjects is a nested dictionary.
    "marks": {
        "physics"  : 90,
        "chemistry": 86,
        "math"     : 96.5
    },
    "age"  : 23,
    "Adult": True
}

#printing the whole student dictionary
print(student)

#printing olny marks of all subjects of the student dictionary.
print(student["marks"])

#printing only marks in chemistry of student dictionary.
print(student["marks"]["chemistry"])

#dictionary_name.keys() returns all the keys_name
print(student.keys())

#dictionary_name.values() returns all the values
print(student.values())

#dictionary_name.items() returns all (key, value) pairs as tuples
print(student.items())

#dictionary_name.get("key_name") returns values according to key_name
print(student.get("marks"))

#dictionary_name.update() inserts the specified items to the dictionary.
new_dictionary = {
    "city" : "Dhaka"
}
student.update(new_dictionary)
print(student)

