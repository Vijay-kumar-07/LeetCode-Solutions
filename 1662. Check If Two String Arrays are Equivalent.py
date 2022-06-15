# Question:

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true

word1 = ["a", "cb"]
word2 = ["ab", "c"]

"".join(word1) == "".join(word2)