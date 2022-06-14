# Question:

# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

# In one step, you can delete exactly one character in either string.

# Input: word1 = "sea", word2 = "eat"
# Output: 2

word1 = "sea"
word2 = "ate"

l1 = len(word1)
l2 = len(word2)

dp = [[0]* (l2 +1) for _ in range(l1+1)]

for i in range(1, l2 +1):
    dp[0][i] = i
for j in range(1, l1+1):
    dp[j][0] = j
for i in range(1, l1+1):
    for j in range(1, l2+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1)
dp[i][j]