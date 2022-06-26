# Question:

# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

# Input: s = "abacbc"
# Output: true

s = "abacbc"
def equal(s):
    a,b = [],[]
    for i in s:
        a.append(s.count(i))
    d = dict(zip(s,a))
    value = list(d.values())[0]
    for key in d.items():
        if key[1] == value:
            b.append(True)
        else:
            b.append(False)
    if all(b): return True
    else: return False
equal(s)