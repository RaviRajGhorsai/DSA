"""

Complete quick_sort(nums, low, high):
If low is less than high:
    Partition the input list using the partition function and store the returned "middle" index
    Recursively call quick_sort on the elements left of the pivot (low to middle - 1)
    Recursively call quick_sort on the elements right of the pivot (middle + 1 to high)


"""

def quick_sort(nums: list[int], low: int, high: int) -> None:
    if low < high:
        p = partition(nums, low, high)

        quick_sort(nums, low, p - 1)
        quick_sort(nums, p + 1, high)

"""

partition(nums, low, high):
Set pivot to the element at index high
Set i to the index before low
For each index (j) in range(low, high):
    If the element at index j is less than the pivot:
        Increment i by 1
        Swap the element at index i with the element at index j
Swap the element at index i + 1 with the element at index high (the pivot's position)
Return i + 1 (the pivot's new index)

"""

def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1

