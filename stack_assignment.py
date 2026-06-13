"""

Complete the is_balanced function.

It takes a string as input and returns True if the parentheses in the string are balanced, and False otherwise. Use an instance of the provided Stack class in stack.py to keep track of the parentheses.

"""

from stack import Stack


def is_balanced(input_str: str) -> bool:

    stack = Stack()
    for inp in input_str:
        if inp == "(":
            stack.push(inp)

        elif inp == ")":
            popped = stack.pop()

            if popped is None:
                return False

    val = stack.peek()

    return val is None
