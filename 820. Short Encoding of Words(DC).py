# Question:

# A valid encoding of an array of words is any reference string s and array of indices indices such that:

# words.length == indices.length
# The reference string s ends with the '#' character.
# For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
# Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

# Input: words = ["time", "me", "bell"]
# Output: 10


words = ["time", "me", "bell"]
def minimumLengthEncoding(words):
    words.sort(key=len, reverse=True)
    ans = ""
    for x in words:
        if x+"#" not in ans:
            ans += x + "#"
            print(ans)
    return len(ans)
minimumLengthEncoding(words)