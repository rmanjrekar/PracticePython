"""
Dynamic sliding window
Longest subarray sum < 15
Steps:
    1. set the left, curr_sum and best to -1,0,0
    2. add the items to curr_sum
    3. if the count exceeds the value of k
         - increase left index by 1
         - subtract the curr_sum by the value of left index item
         - continue till the curr_sum >= k
    4. best count will the max of best and current_index - left

"""
nums = [4,2,5,2,0,4,6,7,7,4,4,6,11,3,1,0,0,0,1,4,2]
k = 15

def calc_longest_subarray(nums, k):
    left, curr_sum, best = -1, 0, 0

    for current_index in range(len(nums)):
        curr_sum = curr_sum + nums[current_index]
        #print("Out", curr_sum)
        while curr_sum >= k:
            #print("in")
            left += 1
            curr_sum -= nums[left]
            #print("Inside", curr_sum)
        print("left ", left)
        best = max(best, current_index - left)
    return best

print(calc_longest_subarray(nums,k))