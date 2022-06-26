# Question:

# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12

cardPoints = [1,79,80,1,1,1,200,1]
k = 3
def MaxScore(cardPoints, k):
    total_sum = sum(cardPoints)
    n = len(cardPoints)
    m = n-k
    if m == 0:
        return total_sum
    window_sum = sum(cardPoints[:m])
    min_window_sum = window_sum
    j = 0
    for i in range(m, n):
        window_sum += cardPoints[i] - cardPoints[j]
        min_window_sum = min(window_sum, min_window_sum)
        j += 1
    return total_sum - min_window_sum
MaxScore(cardPoints, k)