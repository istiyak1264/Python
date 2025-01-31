#!/bin/python3
lists = [3, 1, 9, 7, 5, 11, 17]

#lists.append(13) will add 13 after 17. If we append 15, it will 15 after 13.
lists.append(13)
lists.append(15)
print("Given list:", lists)

#lists.reverse() will reverse the lists.
lists.reverse()
print("Given list in reverse order:",lists)

#lists.sort() will sort the lists in ascending order.
lists.sort()
print("Sorting the list in ascending order:",lists)

#lists.sort(reverse = True) will sort the list in descending order.
lists.sort(reverse = True)
print("Sorting the list is descending order:", lists)

#lists.insert(index_no, element) will insert element at the specified index no.
lists.insert(0,17)
print("Inserting 0 at index[0]:", lists)

#lists.remove(17) will remove first occurance of 17
#before removing: [17, 17, 15, 13, 11, 9, 7, 5, 3, 1]
#after removing : [17, 15, 13, 11, 9, 7, 5, 3, 1]
lists.remove(17)
print("Removing the first occurance of 17:", lists)

#lists.pop(index_no) will remove the index_no
lists.pop(5)
print("After poping index no 5:", lists)