# Question:

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Input: n = 2
# Output: [0,1,1]

# Dynamic approach
def countBits(n):
    dp = [0]*(n+1)
    offset = 1
    for i in range(1,n+1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1+ dp[i-offset]
    return dp

countBits(2)

# Naive approach
n = 2
a = []
for i in range(n+1):
    b = bin(i)[2:]
    a.append(b.count(str(1)))
a