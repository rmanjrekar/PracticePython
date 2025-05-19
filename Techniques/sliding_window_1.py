"""
Static sliding window
Maximum sum of subarray of size K
Steps:
    1. get the sum of first all elements till 'k'
    2. start the loop from k till end
    3. to get count of current window
        - subtract the item from left
        - add the item from right
"""
nums = [4,2,5,2,1,4,6,7,7,4,4,6,11]
k = 3

def max_sum(nums, k):
    curr = best = sum(nums[:k])

    for i in range(k, len(nums)):
        curr = curr + nums[i] - nums[i-k]
        best = max(best, curr)
    return best

print(max_sum(nums, k))
