# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

# Input: nums = [4,2,4,5,6]
# Output: 17

# Solution:

nums = [4,2,4,5,6]
seen = set()
res = i = tot = 0
for j in range(len(nums)):
    x = nums[j]
    while i < j and x in seen:
        seen.remove(nums[i])
        tot -= nums[i]
        i += 1
    tot += x
    seen.add(x)
    res = max(res, tot)
res