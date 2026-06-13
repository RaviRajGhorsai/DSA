"""

In this chapter we'll build a stack from scratch! A stack will be useful at LockedIn when we need undo/redo functionality. For example, a user can add other users to their "connections" list, and then undo the last connection they added. Stacks are a great way to implement undo functionality.

For now, we'll just focus on two methods: push and size. Notice that the Stack class already has a constructor and 
the underlying List that we'll use to store items.

Complete the push method. It should add an item to the top of the stack. The "top" of the stack is the end of the list in our implementation.
Complete the size method. It should return the number of items in the stack.


Pop and Peek
Now that we can add items to our stack, we need to be able to view the top item, and remove the top item.

Assignment
Complete the peek method. It should return the top item from the stack without modifying the stack. If the stack is empty, return None.
Complete the pop method. It should remove and return the top item from the stack. If the stack is empty, return None.



"""

from typing import Any


class Stack:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.append(item) 

    def size(self) -> int:
        return len(self.items) 

    def pop(self):
        if len(self.items) == 0:
            return None

        val = self.items[-1]

        del self.items[-1]

        return val

    def peek(self):
        if len(self.items) == 0:
            return None

        return self.items[-1]  # -1 returns last element in the list (can use length of list to return too)


