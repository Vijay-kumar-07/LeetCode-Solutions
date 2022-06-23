# Question:

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

nums = [3,2,3,1,2,4,5,5,6]
k = 4
def LargestElement(nums, k):
    for _ in range(k-1):
        nums.remove(max(nums))
    return max(nums)

LargestElement(nums, k)