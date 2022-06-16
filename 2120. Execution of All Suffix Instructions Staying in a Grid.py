# Question:

# There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1). You are given the integer n and an integer array startPos where startPos = [startrow, startcol] indicates that a robot is initially at cell (startrow, startcol).

# You are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot: 'L' (move left), 'R' (move right), 'U' (move up), and 'D' (move down).

# The robot can begin executing from any ith instruction in s. It executes the instructions one by one towards the end of s but it stops if either of these conditions is met:

# The next instruction will move the robot off the grid.
# There are no more instructions left to execute.
# Return an array answer of length m where answer[i] is the number of instructions the robot can execute if the robot begins executing from the ith instruction in s.

# Input: n = 3, startPos = [0,1], s = "RRDDLU"
# Output: [1,5,4,3,1,0]

n = 2
startPos = [1,1]
s = "LURD"

m = {"L":(0,-1),"R":(0,1),"U":(-1,0),"D":(1,0)}
a = []
for i in range(len(s)):
    x = startPos[0]
    y = startPos[1]
    count = 0
    for c in s[i:]:
        x += m[c][0]
        y += m[c][1]
        if 0 <= x < n and 0 <= y < n: count += 1
        else: break
    a.append(count)
a
