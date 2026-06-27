def subset_sum(nums: list[int], target: int) -> bool:
    return find_subset_sum(nums, target, len(nums) - 1)

def find_subset_sum(nums: list[int], target: int, index: int) -> bool:
    if target == 0:
        return True

    if index < 0 and target != 0:
        return False

    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    
    result1 = find_subset_sum(nums, target, index - 1)

    result2 = find_subset_sum(nums, target - nums[index], index - 1)

    return result1 or result2
