###LINKED LIST

class Node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None #next node default to None



class LinkedList:
    def __init__(self):
        self.head = Node(None) #head node, unaccesable by the user
        self.size = 0  #size of the linked list


    # adds another node that contains (param:data) to the end of the list
    def append(self, obj):
        new_node = Node(obj)
        current = self.head
        self.size += 1
        while (current.next != None):
            current = current.next

        current.next = new_node
    

    # prints out the items of the linked list in a regular list
    def display(self):
        items = []
        current = self.head
        while (current.next != None):
            items.append(current.next.data)
            current = current.next

        print(items)
    

    # returns the length of the linked list as an integer
    def length(self):
        count = 0
        current = self.head
        while (current.next != None):
            count += 1
            current = current.next
        
        return count
    

    # returns the value of the node at (param:index)
    def get(self, index):
        if (self.size >= index >= 0):
            current = self.head
            for i in range(0, index + 1):
                current = current.next
            return current.data
        else:
            return IndexError


    # deletes node at certain index
    def delete(self, index=0):
        count = 0
        last_node = self.head
        while True:
            current_node = last_node.next
            if (count == index):
                last_node.next = current_node.next
                return

            count += 1
            last_node = last_node.next


    # deletes the node at the index(default to -1) of linked list and returns it
    def pop(self, index=None):
        if (index != None):
            popped_node = self.get(index) #gets the data of the node at (param:index)
            self.delete(index)    
            return popped_node
        else:
            current = self.head
            count = 0
            while (current.next != None):
                current = current.next
                count += 1
            popped_node = current.data
            self.delete(count)
            return popped_node
        

    # converts the linked list into a list and returns the list
    def convert_list(self):
        items = []
        current = self.head
        while (current.next != None):
            items.append(current.next.data)
            current = current.next
        
        return items


    # converts the linked list into a string
    def convert_string(self):
        string = ''.join([str(i) for i in self.convert_list()]) #turns the converted list into a string
        return string


    # use [] instead of (method:self.get) to get item at certain index
    def __getitem__(self, index):
        return self.get(index)


    # checks if (param:self) and (param:value) are the same
    def __eq__(self, value):
        if (self == value):
            return True
        else:
            return False
    

    # checks if (param:self) is greater than or equal to (param:value)
    def __ge__(self, value):
        if (self >= value):
            return True
        else:
            return False
    

    # checks if (param:self) is greater than (param:value)
    def __gt__(self, value):
        if (self > value):
            return True
        else:
            return False
    

    # checks if (param:self) is less than or equal to (param:value)
    def __le__(self, value):
        if (self <= value):
            return True
        else:
            return False


    # checks if (param:self) is less than or equal to (param:value)
    def __lt__(self, value):
        if (self < value):
            return True
        else:
            return False