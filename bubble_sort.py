"""

Here's the pseudocode:

Set swapping to True
Set end to the length of the input list
While swapping is True:
Set swapping to False
For i from the 2nd element to end:
If the (i-1)th element of the input list is greater than the ith element:
Swap the (i-1)th element and the ith element
Set swapping to True
Decrement end by one
Return the sorted list

"""

def bubble_sort(nums: list[int]) -> list[int]:
    
    swapping = True
    end = len(nums)

    while swapping:
        swapping = False

        for i in range(1, end):
            if nums[i-1] > nums[i]:
                a = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = a

                swapping = True

        end -= 1

    return nums


