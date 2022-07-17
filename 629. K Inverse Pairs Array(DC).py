# Question:

# For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

# Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

# Input: n = 3, k = 0
# Output: 1

n = 3
k = 0

def kInversePairs(n, k):
        dp, mod = [1]+[0] * k, 1000000007
        
        for i in range(n):
            tmp, sm = [], 0
            for j in range(k + 1):
                sm+= dp[j]
                if j-i >= 1: sm-= dp[j-i-1]
                sm%= mod
                tmp.append(sm)
            dp = tmp
            
        return dp[k]

kInversePairs(n, k)