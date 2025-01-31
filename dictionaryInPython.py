#!/bin/python
student_dictionary = {
    "name"    : ("Istiyak", "Imran", "Rakib", "Koushik", "Nasimul"),
    "subjects": ("physics", "chemistry", "math", "biology", "English"),
    "marks"   : [67.5, 82, 74.5, 55, 87.5],
    "roll"    : 230103,
    "age"     : 23,
    "is_adult": True,
}
#dictionaries in python are mutable
#printing the full dictionary.
print(student_dictionary)

#printing the type of student_dictionary
print(type(student_dictionary))

#printing the "key" : value separatedly.
print(student_dictionary["name"])
print(student_dictionary["subjects"])
print(student_dictionary["marks"])
print(student_dictionary["roll"])
print(student_dictionary["age"])
print(student_dictionary["is_adult"])

null_dictionary = {}
print(null_dictionary)
