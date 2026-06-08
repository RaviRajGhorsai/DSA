"""

merge_sort() pseudocode
Input: A, an unsorted list of integers

If the length of A is less than 2, it's already sorted so return it
Split the input array into two halves down the middle
Call merge_sort() twice, once on each half
Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls

"""


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    middle = len(nums)//2
    left = nums[:middle]
    right = nums[middle:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


"""

merge() pseudocode
Inputs: A and B. Two sorted lists of integers

Create a new final list of integers.
Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
Use a loop to compare the current elements of A and B:
    While i < len(A) and j < len(B), compare A[i] and B[j].
    Append the smaller or equal value to final.
    Increment the index for the list you just took from.
    Stop when either list is exhausted.
After comparing all the items, there may be some items left over in either A or B. Add those extra items to the final list.
Return the final list.

"""

def merge(first: list[int], second: list[int]) -> list[int]:
    final = []

    i=j=0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
        

    final.extend(first[i:])   # or use loop instead to with i and j to append remaining elements.
    final.extend(second[j:])

    return final


