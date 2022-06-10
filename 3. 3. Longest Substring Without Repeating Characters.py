# Question:
# Given a string s, find the length of the longest substring without repeating characters.

#Input: s = "abcabcbb"
#Output: 3

s = "abcabcbb"
def length(s):
    last_seen = {}
    l = 0
    max_length = 0
    for r in range(len(s)):
        if s[r] in last_seen:
            l = max(last_seen[s[r]], l)
            
        last_seen[s[r]] = r+1
        max_length = max(max_length, r-l+1)
    return max_length
length(s)