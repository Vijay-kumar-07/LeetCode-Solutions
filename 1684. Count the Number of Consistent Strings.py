# Question:

# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.

# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2

allowed = "fstqyienx"
words = ["n","eeitfns","eqqqsfs","i","feniqis","lhoa","yqyitei","sqtn","kug","z","neqqis"]


cnt = 0
for i in words:
    for j in i:
        if j not in allowed:
            cnt += 1
            break
len(words) - cnt