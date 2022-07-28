# Question:

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Input: s = "anagram", t = "nagaram"
# Output: true

s = "anagram"
t = "nagaram"
def validAnagram(s,t):
    d1,d2 = {},{}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        d1[s[i]] = s.count(s[i])
        d2[t[i]] = t.count(t[i])
    if d1 == d2:
        return True
    else:
        return False
validAnagram(s,t)

#Another approach
from collections import Counter
def validAnagram(s,t):
    return Counter(s) == Counter(t)
validAnagram(s,t)