# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11

a = [[2],[3,4],[6,5,7],[4,1,8,3]]
def dfs(level, i):            
    return 0 if level >= len(a) else a[level][i] + min(dfs(level + 1, i), dfs(level + 1, i+1))        
dfs(0, 0)