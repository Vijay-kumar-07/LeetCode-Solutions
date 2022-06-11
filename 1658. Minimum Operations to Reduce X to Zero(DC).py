# You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.


# Input: nums = [1,1,4,2,3], x = 5
# Output: 2

# Solution:

nums = [1,1,4,2,3]
x = 5
def minOperations(nums, x):
    target = sum(nums) - x
    curr_sum, max_len = 0, 0
    start_idx = 0
    found = False
    for end_idx in range(len(nums)):
        curr_sum += nums[end_idx]
        while start_idx <= end_idx and curr_sum > target:
            curr_sum -= nums[start_idx]
            start_idx += 1
        if curr_sum == target:
            found = True
            max_len = max(max_len, end_idx - start_idx + 1)
            
    return len(nums) - max_len if found else -1
    
    
    
minOperations(nums, x)