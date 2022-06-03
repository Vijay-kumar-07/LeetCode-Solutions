# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]

class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        
    def sumRegion(self, row1, col1, row2, col2):
        a = []
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                a.append(self.matrix[i][j])
        return sum(a)
    
    
numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
numMatrix.sumRegion(2,1,4,3)





# Another approach:


class NumMatrix:
    def __init__(self, matrix):
        m,n = len(matrix),len(matrix[0])
        self.dp = [[0]*(1+n) for _ in range(1+m)]
        for i in range(1,1+m):
            for j in range(1,1+n):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] + matrix[i-1][j-1] - self.dp[i-1][j-1]
        
    def sumRegion(self, row1, col1, row2, col2):
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] +self.dp[row1][col1]
    
    
numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
numMatrix.sumRegion(2,1,4,3)