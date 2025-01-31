#!/bin/python3

#set is the collection of unordered items.
#Each value in set must be unique and immutable.

collection = {3, 7, 3, 1, 2, 2, 4, 3, 9, 9, 'a', 'b', 'b', 'c', 'd', 'e', 'e'}
#if we insert a value multiple times. Set will ignore the duplicate items and 
#it will print the items single time
print(collection)
print(type(collection))

#len() will be printed ignoring the duplicate items
print(len(collection))

#systax of declaring empty set:  set_name = set()
#if we declare set like this: set_name = {} ,it will be a empty dictionary.
collection2 = set()
print(collection2)
print(type(collection2))


#set_name.add(element) will add an element in the set
#we can pass tuples and strings in the set but we can't pass list in the set.
collection.add(5)
collection.add((20, 22, 29))#passing tuples in the set
print(collection)

#set_name.remove(element) will remove the element from the set
collection.remove('a')
print(collection)

#set_name.pop() removes a random value from the set.
collection.pop()
print(collection)

#set_name.clear(element) will empties the set
collection.clear()
print(collection)


#set1.union(set2) combines both set1 and set2
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.union(set2))

#set1.intersection(set2) returns the common items between the set1 and set2
print(set1.intersection(set2))