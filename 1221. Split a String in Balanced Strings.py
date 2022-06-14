# Question:

# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it in the maximum amount of balanced strings.

# Return the maximum amount of split balanced strings.

# Input: s = "RLRRLLRLRL"
# Output: 4

s = "RLRRLLRLRL"
def balancedStringSplit(s):
    flag = 0
    res = 0
    for i in s:
        if i == "R":
            flag += 1
        elif i == "L":
            flag -= 1
        if flag == 0:
            res += 1
    return res
balancedStringSplit(s)