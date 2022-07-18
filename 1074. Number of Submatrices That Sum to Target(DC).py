# Question:

# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4

 matrix = [[0,1,0],[1,1,1],[0,1,0]]
 target = 0

 def numSubmatrixSumTarget(matrix, target):
        n,m = len(matrix),len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        
        # make prefix sum for every row
        for i in range(n):
            for j in range(m):
                dp[i][j] = matrix[i][j] + (dp[i][j-1] if j-1>=0 else 0)
        # print(*dp,sep="\n")        
        ans = 0
        # for every column see row sum
        for i in range(m):
            for j in range(i,m):
                d = {0:1}
                s = 0
                for r in range(n):
                    s += dp[r][j] - (dp[r][i-1] if i-1>=0 else 0)
                    if s-target in d:
                        ans += d[s-target] 
                        
                    if s in d:
                        d[s] += 1
                    else:
                        d[s] = 1
                        
        return ans
numSubmatrixSumTarget(matrix, target)