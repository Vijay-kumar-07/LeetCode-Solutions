# You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

# You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

# While moving from building i to building i+1 (0-indexed),

# If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
# If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
# Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

 

#  Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
# Output: 7

heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
import heapq
l = []
sum = 0
for i in range(1, len(heights)):
    h = heights[i] - heights[i-1]
    if h>0:
        if len(l)<ladders:
            heapq.heappush(l,h)
        elif l and h>l[0]:
            sum += l[0]
            heapq.heappop(l)
            heapq.heappush(l,h)
        else:
            sum += h
        if sum>bricks:
            print(i-1)
print(i)