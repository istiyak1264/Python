#!/bin/python3

class Person:
    name = "Imran"
    """def changeName(self, name):
        self.name = name it will not work on Person.name
        Person.name = name it is a technique and below is the best technique
        it will change class attribute name = "Imran" to name = "Istiyak"
        self.__class__.name = name """

    @classmethod #this line is called decorator
    def changeName(cls, name):
        #here cls is refering to the class
        cls.name = name

p1 = Person()
p1.changeName("Istiyak")

print(p1.name)
print(Person.name)