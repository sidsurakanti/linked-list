class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node(None) #head node, unaccesable by the user
        self.size = 0  #size of the linked list
    
    # adds another node that contains (param:data) to the end of the list
    def append(self, obj):
        new_node = node(obj)
        current = self.head
        self.size += 1
        while current.next != None:
            current = current.next

        current.next = new_node
    
    # prints out the items of the linked list in a regular list
    def display(self):
        items = []
        current = self.head
        while current.next != None:
            items.append(current.next.data)
            current = current.next

        print(items)
    
    # returns the length of the linked list as an integer
    def length(self):
        count = 0
        current = self.head
        while current.next != None:
            count += 1
            current = current.next
        
        return count
    
    # returns the value of the node at (param:index)
    def get(self, index):
        if self.size > index > 0:
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
            if count == index:
                last_node.next = current_node.next
                return

            count += 1
            last_node = last_node.next
    
    # use [] instead of (method:self.get) to get item at certain index
    def __getitem__(self, index):
        return self.get(index)
    

ll = linked_list()
ll.append(2)
ll.append("hello")
print(ll[1])