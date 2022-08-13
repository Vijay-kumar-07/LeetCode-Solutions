# Question:

# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

# You can return the answer in any order.

# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m = len(words)
        k = len(words[0])
        res = []
        
        for i in range(k):
            left = i
            d = Counter(words)
            
            for j in range(left, len(s) + 1 - k, k):
                word = s[j: j + k]
                d[word] -= 1
                
                while d[word] < 0:
                    d[s[left: left + k]] += 1
                    left += k
                if left + k * m == j + k:
                    res. append(left)
        
        return res
        