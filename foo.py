from linked_list import LinkedList


# appending to a linked list
ll1 = LinkedList()
ll1.append(1)
ll1.append("2")
ll1.append(3.0)
print(f"new linked list: {ll1}\n")  # [1, 2, '3', 4.0]

# extending a linked list
ll2 = LinkedList()
print(f"unextended ll2: {ll2}") 
ll2.extend([1, 2, 3])
ll2.extend((4, 5, 6))
ll2.extend({7, 8, 9})
print(f"extended ll2: {ll2}\n")  # [1, 2, 3, 4, 5, 6, 8, 9, 7]

# sorting a linked list
ll3 = LinkedList((1, 4, 2, 3))
print(f"unsorted ll3: {ll3}")  # [1, 4, 2, 3]
ll3.sort()
print(f"sorted ll3: {ll3}\n")  # [1, 2, 3, 4]

# popping and inserting
ll4 = LinkedList([3, 4, 5])
print(f"ll4: {ll4}")  # [3, 4, 5]
popped_item = ll4.pop(0)
print(f"ll4 without index 0: {ll4}")
ll4.insert(popped_item)
print(f"ll4 after inseting popped_item: {ll4}\n")

# general methods
ll = LinkedList([1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"object at the 4th index of ll: {ll.get(4)}") 
print(f"# of instances of 1: {ll.count(1)}")
del ll[0]
print(f"ll after deleting object at index 0: {ll}")
ll.clear()
print(f"ll after clearing it: {ll}")
