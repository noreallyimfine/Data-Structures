import sys
sys.path.append('queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # each object should be its own BST
        bst_value = BinarySearchTree(value)
        # if lower than current node
        if self.value >= value:
            # if it doesnt have a child, this value becomes child
            if not self.left:
                self.left = bst_value
            else:
            # recursion with the left child
                return self.left.insert(value)
        # if greater than current node
        elif self.value < value:
            # if it doesnt have child, this value becomes child
            if not self.right:
                self.right = bst_value
            else:
                # recursion with the right child
                return self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case - found target:
        if self.value == target:
            # return true
            return True

        # if current value is higher than target
        elif self.value > target:
            if self.left:
                return self.left.contains(target)
        elif self.value < target:
            if self.right:
                return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        highest = self.value
        current = self
        while current.right:
            current = current.right
        highest = current.value
        return highest

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        current = self.value
        right = self.right
        left = self.left

        self.value = cb(current)
        print(self.value)
        if right:
            right.for_each(cb)
        
        if left:
            left.for_each(cb)
        
    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
