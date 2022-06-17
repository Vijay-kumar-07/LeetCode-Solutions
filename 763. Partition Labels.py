# Question:

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]

s = "ababcbacadefegdehijhklij"
L = len(s)
last = {s[i]: i for i in range(L)}
print(last)
i = 0
ans = []
while i < L:
    end = last[s[i]]
    j = i + 1
    while j < end:
        if last[s[j]] > end:
            end = last[s[j]]
        j += 1
    ans.append(end - i + 1)
    i = end + 1
ans