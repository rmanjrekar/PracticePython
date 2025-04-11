"""
Sorted array
Steps:
    1. set low and high pointer to 0 and last index of array respectively
    2. do below till low is less than or equal to high
        - calculate mid => (low+high)//2
        - if mid is same as target then return the mid index
        - if mid is smaller than target then set low pointer to mid+1
        - if mid is greater than target then set high pointer to mid-1
"""

def binary_search(nums,k):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == k:
            return mid
        elif k > nums[mid]:
            low = mid+1
        else:
            high = mid-1

    return f"Not found"

nums = [2,3,4,5,6,7,8,9,10,11]
target = 8

print("Output--->" , binary_search(nums, target))