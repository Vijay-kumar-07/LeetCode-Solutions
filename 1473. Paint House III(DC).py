# Question:

# There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

# A neighborhood is a maximal group of continuous houses that are painted with the same color.

# For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
# Given an array houses, an m x n matrix cost and an integer target where:

# houses[i]: is the color of the house i, and 0 if the house is not painted yet.
# cost[i][j]: is the cost of paint the house i with the color j + 1.
# Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.

# Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# Output: 9

houses = [0,0,0,0,0]
cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]
m = 5
n = 2
target = 3
def minCost(houses, cost, m, n, target):
        dp = [[[math.inf for k in range(target + 1)] for j in range(n + 1)] for i in range(m + 1)]
        for j in range(n + 1):
            dp[0][j][0] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
			    # The current house has already been painted, no need to consider other colors
                if houses[i - 1] and houses[i - 1] != j:
                    continue
                for k in range(1, target + 1):
                    ls = [dp[i - 1][jj][k - 1] for jj in range(1, n + 1) if jj != j] + [dp[i - 1][j][k]]
                    dp[i][j][k] = min(ls)
                    if houses[i - 1] == 0: # Only add paint cost if it hasn't been painted before
                        dp[i][j][k] += cost[i - 1][j - 1]
        ans = min([dp[m][j][target] for j in range(1, n + 1)])
        if ans == math.inf:
            return -1
        return ans

minCost(houses, cost, m, n, target)