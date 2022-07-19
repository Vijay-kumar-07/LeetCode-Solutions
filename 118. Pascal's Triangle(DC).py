# Question:

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

numRows = 1
result = [[1] * (row + 1) for row in range(numRows)]
for row in range(2, numRows):
    for col in range(1, row):
        result[row][col] = result[row-1][col-1] + result[row-1][col]
print(result)
    
