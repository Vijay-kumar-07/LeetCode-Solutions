# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

#Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

#Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

# Solution:

n = 4
state = [["."] * n for _ in range(n)]
res = []
visited_cols = set()
visited_diagonals = set()
visited_antidiagonals = set()

def backtrack(r):
    if r == n:
        res.append(["".join(row) for row in state])
        return
    for c in range(n):
        diff = r-c
        _sum = r+c
        
        if not (c in visited_cols or diff in visited_diagonals or _sum in visited_antidiagonals):
            visited_cols.add(c)
            visited_diagonals.add(diff)
            visited_antidiagonals.add(_sum)
            state[r][c] = "Q"
            backtrack(r+1)
            
            visited_cols.remove(c)
            visited_diagonals.remove(diff)
            visited_antidiagonals.remove(_sum)
            state[r][c]= "."
backtrack(0)
res