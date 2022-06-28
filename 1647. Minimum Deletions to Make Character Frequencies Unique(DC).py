# Question:

# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

# Input: s = "aab"
# Output: 0

s = "aaabbbcc"
def minDeletions(s):
    frequencies = sorted(Counter(s).values(), reverse=True)
    total_deletions = 0
    next_unused_freq = len(s)
    for freq in frequencies:
        next_unused_freq = min(next_unused_freq, freq)
        total_deletions += freq - next_unused_freq
        if next_unused_freq > 0:
            next_unused_freq -= 1
    return total_deletions
minDeletions(s)