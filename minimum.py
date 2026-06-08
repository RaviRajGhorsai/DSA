def find_minimum(nums: list[int]) --> float | None:

    if len(nums) == 0:
        return None

    min = float("inf")

    for num in nums:
        if num < min:
            min = num

    return min
