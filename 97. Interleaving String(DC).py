# Question:

# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.

# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
def isInterleave(s1, s2, s3):
        n, m = len(s1), len(s2)
        if n + m != len(s3): return False
        dp = [True] * (m+1)
        for i in range(1, m+1):
            dp[i] = dp[i-1] and s2[i-1] == s3[i-1]
        for i in range(n):
            dp[0] = dp[0] and s1[i] == s3[i] 
            for j in range(m):
                dp[j+1] = (dp[j+1] and s1[i] == s3[i+j+1]) or (dp[j] and s2[j] == s3[i+j+1])
        return dp[-1]

isInterleave(s1, s2, s3)