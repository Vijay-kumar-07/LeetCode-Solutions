# Question:

# You are given two string arrays words1 and words2.

# A string b is a subset of string a if every letter in b occurs in a including multiplicity.

# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.

# Return an array of all the universal strings in words1. You may return the answer in any order.

# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
# Output: ["facebook","google","leetcode"]

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
def wordsubsets(words1, words2):
    mc = Counter()
    for w in words2:
        t = Counter(w)
        for i in t:
            mc[i] = max(mc[i],t[i])
    ans = []
    for w in words1:
        t = Counter(w)
        for i in mc:
            if mc[i]>t[i]:
                break
        else:
            ans.append(w)
    return ans


wordsubsets(words1, words2)