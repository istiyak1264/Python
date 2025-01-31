#!/bin/python3

#Lists is like array.
lists = ["Istiyak", 230103, 85, "Pabna"]
#if we start counting from left to right-> list will start from index 0.
#e.g: lists[0] = "Istiyak", lists[1] = 230103 , lists[2] = 85, lists[3] = "Pabna"
print(type(lists))

#String can't be changed like below but lists can be changed like below.
lists[0] = "Ahmed Imran"
lists[3] = "Sirajganj"
print(len(lists))
print(lists[:1])
print(lists[:3])
print(lists[:len(lists)])

#if we start counting from Right to Left-> list will start from index -1.
#e.g: lists[-1] = "Pabna", lists[-2] = 85, lists[-3] = 230103, lists[-4] = "Istiyak"
print(lists[-4:-1])
print(lists[-4:-2])
print(lists[-3:-1])



