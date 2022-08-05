# Question:

# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.

nums = [1,2,3]
target = 4

dp = [0] * (target+1)
dp[0] = 1
for i in range(1, target+1):
    for num in nums:
        num_before = i - num
        if num_before >= 0:
            dp[i] += dp[num_before]
dp[target]