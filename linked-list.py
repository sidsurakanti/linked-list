from node import Node


class LinkedList:
    def __init__(self):
        self.head = Node()  # sets head node as a empty instance of the class Node so it's inaccessible to the user
        self.size = 0  # size of the linked list instance

    def append(self, data, index: int = None):
        """adds :param data: to the index :param index: of the linked list"""
        data = Node(data)  # creates a new instance of the class Node with data <data>
        current = self.head  # sets current node as the head node since it's the first node in the linked list
        index = index or self.size  # sets index to <index> if <index> otherwise to the length of the linked list
        count = 0

        # while the index of the current node is smaller than index
        while count < index:
            current = current.next
            count += 1

        current.next = data
        self.size += 1
        return

    def __len__(self):
        """Dunder-method for len() built-in function"""
        return self.size

    def __str__(self):
        """Dunder-method for printing"""
        current = self.head  # sets current node to <self.head>
        data = []

        # loops thru all the nodes in the list and adds the node's data to <data>
        while current.next is not None:
            data.append(current.next.data)
            current = current.next

        return str(data)

    # TODO: Add support for slicing
    def __getitem__(self, index):
        """Dunder-method for slicing"""
        current = self.head  # sets current node to <self.head>
        count = 0

        # while index of current node is smaller than the <index>
        while count < index:
            current = current.next
            count += 1
        current = current.next

        return current.data


l1 = LinkedList()
l1.append(0)
l1.append(1)
print(l1[0])

