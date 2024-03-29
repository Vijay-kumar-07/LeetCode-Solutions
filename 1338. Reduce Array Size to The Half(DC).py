# Question:

# You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

# Return the minimum size of the set so that at least half of the integers of the array are removed.

# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)      # Use Counter() to get numbers and their frequency
        num_freq = sorted(cnt.values(), reverse=True)  # Sort dictionary by their frequency (descending order)
        
        half_size = len(arr) // 2
        ans = 0
        
        while half_size > 0:
            half_size -= num_freq[ans]
            ans += 1
        
        return ans
        