class Node:
    def __init__(self, data: object = None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        assert isinstance(other, Node)
        return self.data == other.data

    def __lt__(self, other):
        assert isinstance(other, Node)
        return self.data < other.data

    def __gt__(self, other):
        assert isinstance(other, Node)
        return self.data > other.data

    def __le__(self, other):
        assert isinstance(other, Node)
        return self.data <= other.data

    def __ge__(self, other):
        assert isinstance(other, Node)
        return self.data >= other.data
