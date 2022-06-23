# Question:

# You are given a string s. Reorder the string using the following algorithm:

# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

# Return the result string after sorting s with this algorithm.

# Input: s = "aaaabbbbcccc"
# Output: "abccbaabccba"


a = []
s = "aaaabbbbcccc"
str_ = ""
for i in s:
    a.append(s.count(i))
dict_ = dict(zip(s,a))
lst = sorted([[x,dict_[x]]for x in dict_])
for x in range(0, len(s)//2+1):
    for i in range(0, len(lst)):
        if lst[i][1] > 0:
            str_ += lst[i][0]
            lst[i][1] -= 1
    for i in range(len(lst)-1,-1,-1):
        if lst[i][1] >0:
            str_ += lst[i][0]
            lst[i][1] -= 1
str_