# Question:
# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

# In one move, you can increment or decrement an element of the array by 1.

# Test cases are designed so that the answer will fit in a 32-bit integer.

# Input: nums = [1,2,3]
# Output: 2

nums = [1,2,3]
def minMoves(nums):
    n = len(nums)
    nums.sort()
    median = nums[n//2]
    res = 0
    for n in nums:
        res += abs(n - median)
    return res

minMoves(nums)