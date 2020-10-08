import copy as cp

from node import Node


class LinkedList:
    def __init__(self, data=None, iterable=True):
        self.head = Node()  # empty instance of class Node
        self.size = 0  # size of the linked list instance
        if data:
            self.extend(data) if iterable else self.append(data)

    def append(self, data): 
        """Adds data to the end of the linked list"""
        self.insert(data)
        self.size += 1

    def get(self, index: int = 1):
        """Gets the data of the node at :param index:"""
        index = self.size - (index * -1) if index < 0 else index

        if 0 <= index <= (self.size - 1):
            current = self.head  # sets current node to <self.head>
            count = 0

            # while index of current node is smaller than the <index>
            while count < index:
                current = current.next
                count += 1

            current = current.next
            return current

    def display(self):
        """Returns the data of all the nodes in the linked list"""
        current = self.head  # sets current node to <self.head>
        data = []

        # loops thru all the nodes in the list and adds the node's data to <data>
        while current.next is not None:
            data.append(current.next.data)
            current = current.next

        return data

    def insert(self, data, index: int = None):
        """Inserts data to index :param index: of the linked list"""
        try:
            data = Node(data)
            index = index or self.size
            current = self.head
            count = 0

            while count < index:  # while index is greater than count
                current = current.next
                count += 1
            last_node = current.next
            current.next = data
            current.next.next = last_node
            return

        except AttributeError:
            print('Please provide a valid index')

    def count(self, value):
        """Counts the no. of times :param value: appears in the linked list"""
        items = self.display()
        return items.count(value)

    def pop(self, index: int = 0):
        """Deletes the node at :param index: and returns its data"""
        item = self.get(index).data
        self.delete(index)
        return item

    def clear(self):
        """Clears the linked list"""
        self.head = Node()
        self.size = 0

    def extend(self, iterable):
        """Extends the linked list with :param iterable:"""
        # loops thru each item in <iterable> and adds it to the linked list
        for item in iterable:
            self.append(item)

        return

    def sort(self):
        """Sorts the linked list in ascending order"""
        lst = self.display()
        self.clear()
        self.extend(sorted(lst))
        return

    def delete(self, key=0):
        """Deletes an object from the linked list"""
        # if <key> is a instance of class int
        if isinstance(key, int):
            last_node = self.head
            count = 0

            while True:
                current_node = last_node.next
                if count == key:
                    last_node.next = current_node.next
                    self.size -= 1
                    return

                count += 1
                last_node = last_node.next

        # if <key> is a instance of class slice
        elif isinstance(key, slice):
            items = self.display()
            length = len(items[key])
            del items[key]
            self.clear()
            self.extend(items)
            self.size -= length

            return

    def copy(self):
        """Returns a copy of the linked list"""
        return self.__copy__()

    def deepcopy(self):
        """Returns a deepcopy of the linked list"""
        return self.__deepcopy__()

    def __del__(self):
        """Dunder method for deleting an instance of the LinkedList class"""
        del self
        return

    def __len__(self):
        """Dunder-method for the built-in len() function"""
        return self.size

    def __str__(self):
        """Dunder-method for printing"""
        return str(self.display())

    def __copy__(self):
        lst = LinkedList()
        lst.extend(self.display())
        return lst

    def __deepcopy__(self):
        lst = LinkedList()
        for node in self:
            lst.append(cp.deepcopy(node.data))
        return lst

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.get(key).data

        elif isinstance(key, slice):
            items = self.display()
            return items[key]

    def __delitem__(self, key):
        self.delete(key)

    def __eq__(self, value):
        if self == value:
            return True
        else:
            return False

    def __ge__(self, value):
        if self >= value:
            return True
        else:
            return False

    def __gt__(self, value):
        if self > value:
            return True
        else:
            return False

    def __le__(self, value):
        if self <= value:
            return True
        else:
            return False

    def __lt__(self, value):
        if self < value:
            return True
        else:
            return False
