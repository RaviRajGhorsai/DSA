"""

Here are the implementation details to do it in polynomial time:

The input n represents the index of the desired Fibonacci number.
If n is less than or equal to 1, then return n.
Initialize three variables: grandparent = 0, parent = 1, and a placeholder current to store the new Fibonacci number at each step.
Write a loop that iterates n - 1 times. (For example, if n = 2, one iteration occurs.)
Inside the loop:
    Set current = parent + grandparent
    Adjust the ancestor values (parent and grandparent) to maintain the sequence.
Once the loop completes, return current.

"""

def fib(n: int) -> int:
    if n <= 1:
        return n

    grandparent = 0
    parent = 1
    current = 0 

    for i in range(0, n-1):
        current = grandparent + parent

        grandparent = parent
        parent = current 

    return current
