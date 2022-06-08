# 17.Replace every element with the greatest element on right side

import copy
arr = [16, 17, 4, 3, 5, 2]
arr1 = copy.deepcopy(arr)
a = []
for i in arr1:
    arr.remove(i)
    if len(a) == len(arr1)-1:
        break
    a.append(max(arr))
    
a.append(-1)
for j in a:
    print(j, end = " ")