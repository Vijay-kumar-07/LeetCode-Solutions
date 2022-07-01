# Question:

# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

# Return the maximum total number of units that can be put on the truck.

# Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
# Output: 8

boxTypes = [[1,3],[2,2],[3,1]] 
truckSize = 4

def maxUnits(boxTypes, truckSize):
    boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
    total = 0
    while truckSize > 0 and len(boxTypes) > 0:
        if truckSize >= boxTypes[0][0]:
            total += boxTypes[0][0] * boxTypes[0][1]
            truckSize -= boxTypes[0][0]
            boxTypes.pop(0)
        else:
            total += truckSize * boxTypes[0][1]
            break
    return total

maxUnits(boxTypes,truckSize)