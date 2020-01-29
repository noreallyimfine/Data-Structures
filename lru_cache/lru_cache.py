from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import ListNode


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.storage = DoublyLinkedList()
        self.cache = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.cache:
            # move key to front of cache and return value
            self.storage.move_to_front(self.cache[key])
            value = self.cache[key].value[1]
            return value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.cache:
            new_node = ListNode((key, value))
            self.cache[key] = new_node
            self.storage.move_to_front(new_node)

        else:
            # if cache is full,  delete tail and add new key to head
            if self.size == self.limit:
                oldest = self.storage.remove_from_tail()
                del self.cache[oldest[0]]
                new_node = ListNode((key, value))
                self.storage.add_to_head(new_node)
                self.cache[key] = new_node
            else:
                #new_node = ListNode((key, value))
                self.storage.add_to_head((key, value))
                self.cache[key] = self.storage.head
                self.size += 1
