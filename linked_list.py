"""
This is an implementation of Linked List
"""
class Node:
    """
    A single Node
    """
    def __init__(self, data):
        """
        To initialise a Node with given data
        """
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __len__(self):
        if self.data is str:
            return len(self.data)
        else:
            return 0

class LinkedList:
    """
    A Linked List
    """
    def __init__(self, data = None):
        """
        To initialise a Linked List with given data if any
        """
        if data is not None:
            self.head = Node(data)
            self.current = self.head
        else:
            self.head = None
            self.current = None

    def __str__(self):
        """
        To return the string representation of the Linked List
        """
        res = ''
        node = self.head
        while node is not None:
            res += ' --> ' + str(node)
            node = node.next
        return res[5:]

    def __len__(self):
        """
        To return the length of the Linked List
        """
        size = 0
        node = self.head
        while node is not None:
            size += 1
            node = node.next
        return size

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        curr_node = self.current
        self.current = curr_node.next
        return curr_node

    def append(self, data):
        """
        To append a new data to the List
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.current = self.head
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def remove(self, index):
        """
        To remove a data node for the given index
        """
        i = 0
        node = self.head
        prev_node = node
        while node is not None:
            if i == index:
                next_node = node.next
                if i == 0:
                    self.head = next_node
                else:
                    prev_node.next = next_node
                break
            prev_node = node
            node = node.next
            i += 1

    def insert(self, index, data):
        """
        To insert a data node for the given index
        """
        i = 0
        a_node = Node(data)
        node = self.head
        prev_node = node
        while node is not None:
            if i == index:
                if i == 0:
                    self.head = a_node
                    self.head.next = prev_node
                else:
                    prev_node.next = a_node
                    a_node.next = node
                return
            prev_node = node
            node = node.next
            i += 1

        prev_node.next = a_node
                 