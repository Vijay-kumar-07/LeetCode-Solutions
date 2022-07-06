# Question:

# You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

# horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
# verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

# Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
# Output: 4 

h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]

def maxArea(h, w, horizontalCuts, verticalCuts):
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_width, max_height = max(horizontalCuts[0], h - horizontalCuts[-1]), max(verticalCuts[0], w - verticalCuts[-1])
        
        
        if len(horizontalCuts) > 1:
            for index_1 in range(1, len(horizontalCuts)):
                max_width = max(max_width, horizontalCuts[index_1] - horizontalCuts[index_1 - 1])
        if len(verticalCuts) > 1:
            for index_2 in range(1, len(verticalCuts)):
                max_height = max(max_height, verticalCuts[index_2] - verticalCuts[index_2 - 1])
                
        return (max_height * max_width) % (10**9 + 7)

maxArea(h, w, horizontalCuts, verticalCuts)