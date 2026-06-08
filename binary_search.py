"""
Order Log N
O(log(n)) algorithms are only slightly slower than O(1), but much faster than O(n). They do grow according to the input size, n, but only according to the log of the input.

"""

def binary_search(target: int, arr: list[int]) -> bool:
    low = 0
    high = len(arr) - 1
    

    while low <= high:
        median = (low + high) // 2  # integer division, if result is float converts into int

        if arr[median] == target:
            return True

        elif arr[median] < target:
            low = median + 1

        else:
            high = median - 1

    return False

