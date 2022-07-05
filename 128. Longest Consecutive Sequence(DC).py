# Question:

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Input: nums = [100,4,200,1,3,2]
# Output: 4

nums = [100,4,200,1,3,2]
import heapq
def longestConsecutive(nums):
    max_len = 0
    num_set = set(nums)
    for num in nums:
        if num - 1 not in num_set:
            curr_num = num
            curr_len = 1
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
    return max_len
longestConsecutive(nums)