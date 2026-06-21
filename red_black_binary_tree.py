from typing import Any


class RBNode:
    def __init__(self, val: Any) -> None:
        self.red = False
        self.parent: "RBNode | None" = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self) -> None:
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def rotate_left(self, pivot_parent: RBNode) -> None:
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return

        pivot = pivot_parent.right

        pivot_parent.right = pivot.left

        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent

        if pivot_parent == self.root:
            self.root = pivot

        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot

        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot

        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent: RBNode) -> None:
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return

        pivot = pivot_parent.left

        pivot_parent.left = pivot.right

        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent

        if pivot_parent == self.root:
            self.root = pivot

        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot

        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot

        pivot.right = pivot_parent
        pivot_parent.parent = pivot

    def insert(self, val: Any) -> None:
        new_node = RBNode(val)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None

        current = self.root

        while current != self.nil:
            parent = current

            if new_node.val < current.val:
                current = current.left

            elif new_node.val > current.val:
                current = current.right

            else:
                return

        new_node.parent = parent

        if parent is None:
            self.root = new_node

        elif new_node.val < parent.val:
            parent.left = new_node

        if new_node.val > parent.val:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, new_node: RBNode) -> None:
        current_node = new_node

        while current_node is not self.root and current_node.parent.red:
            parent = current_node.parent

            grand_parent = current_node.parent.parent

            if parent is grand_parent.right:

                uncle = grand_parent.left

                if uncle.red:
                    uncle.red = False
                    parent.red = False

                    grand_parent.red = True

                    current_node = grand_parent
                else:
                    if current_node is parent.left:
                        current_node = parent

                        self.rotate_right(current_node)

                        parent = current_node.parent

                    parent.red = False
                    grand_parent.red = True

                    self.rotate_left(grand_parent)

            elif parent is grand_parent.left:
                uncle = grand_parent.right

                if uncle.red:
                    uncle.red = False
                    parent.red = False

                    grand_parent.red = True

                    current_node = grand_parent

                else:
                    if current_node is parent.right:
                        current_node = parent

                        self.rotate_left(current_node)

                        parent = current_node.parent

                    parent.red = False
                    grand_parent.red = True

                    self.rotate_right(grand_parent)
        
        self.root.red = False
