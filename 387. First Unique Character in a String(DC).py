# Question:

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Input: s = "leetcode"
# Output: 0

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i, v in enumerate(s):
            if c[v] == 1:
                return i
        return -1
        