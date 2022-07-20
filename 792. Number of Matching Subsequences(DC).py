# Question:

# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".

# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

s = "abcde"
words = ["a","bb","acd","ace"]

def numMatchingSubseq(s, words):
        def sub(st):
            pos = -1
            for char in st:
                pos = s.find(char, pos+1)
                if pos == -1: return False
            return True
        return sum(map(sub, words))
numMatchingSubseq(s, words)