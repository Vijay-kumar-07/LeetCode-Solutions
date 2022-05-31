# Daily Challenge:
#Question:

#Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

# Input: s = "00110110", k = 2

#Solution:
s = "00110110"
k = 2
got = set()
for i in range(len(s)-k+1):
    got.add(s[i:i+k])
if len(got) == 2**k:
    print(True)
else:
    print(False)