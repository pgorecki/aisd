class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # wstawia element na poczatek listy
    def insert(self, node):
        if type(node) is not Node:
            raise TypeError("argument node musi byc typu Node")

        current = self.head
        self.head = node
        node.next = current

    def delete(self, node):
        if type(node) is not Node:
            raise TypeError("argument node musi byc typu Node")
        raise NotImplementedError()

    # wyszukuje wezel listy, zawierajacy dane o wartosci data
    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None