"""
O(n) - Order “n”
O(n) is very common - When the number of steps in an algorithm grows at the same rate as its input size, it's classified as O(n)

"""

def find_max(nums: list[float]) -> float:
    max = nums[0]

    for num in nums:
        if num > max:
            max = num
    return max

