# Question:

# There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

# You will start on the 1st day and you cannot take two or more courses simultaneously.

# Return the maximum number of courses that you can take.

# Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# Output: 3

import heapq
courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
courses.sort(key=lambda c:c[1])
A, curr = [],0
for dur, Id in courses:
    heapq.heappush(A, -dur)
    curr += dur
    if curr > Id: curr += heapq.heappop(A)
len(A)