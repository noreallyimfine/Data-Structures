import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        ## if list is empty
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if not self.storage.head:
            return
        else:
            pop = self.storage.remove_from_head()
            self.size -= 1
        return pop

    def len(self):
        return self.size
