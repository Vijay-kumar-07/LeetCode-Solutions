# Question:

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

class Solution:
    def searchRange(nums, target):
        ans=[-1, -1]
        ans[0] = self.find_index(nums, target, 'l')
        ans[1] = self.find_index(nums, target, 'r')
        return ans
        
    def find_index(self, nums, target, method):    # method: leftmost or rightmost
        index = -1
        low, high = 0, len(nums) -1
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] == target:
                index = mid
                # checking the method 
                if method == 'r':
                    low = mid + 1
                elif method == 'l':
                    high = mid - 1
            elif nums[mid] > target: 
                high = mid - 1
            else:
                low = mid + 1
        return index
searchRange(nums, target)
        