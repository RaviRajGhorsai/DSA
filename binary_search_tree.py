"""
Complete the insert method of the BSTNode class. It takes a User object as input and adds it to a new node if the value doesn't already exist in the tree.

If the node doesn't have a value yet, store the given value and return
If the node's value is equal to the given value, just return, no duplicates allowed
If the given value is less than the node's value and the node doesn't have a left child, create a new left child node with the given value and return
If the given value is less than the node's value and the node does have a left child, recursively call insert off of that left child with the given value and return
Since we already checked if the given value is equal to or less than the node, the value must be greater than the node. Handle whether or not the node already has a right child
"""

from typing import Any


class BSTNode:
    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def get_min(self) -> Any:
        min_val = self

        while min_val.left is not None:
            min_val = min_val.left

        return min_val.val

    def get_max(self) -> Any:
        max_val = self

        while max_val.right is not None:
            max_val = max_val.right

        return max_val.val

    def insert(self, val: Any) -> None:
        if self.val is None:
            self.val = val
            return

        elif self.val == val:
            return

        elif val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
                return
            else:
                self.left.insert(val)
                return
        else:
            if self.right is None:
                self.right = BSTNode(val)
                return

            self.right.insert(val)
            return
