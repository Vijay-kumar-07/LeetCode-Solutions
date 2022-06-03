# 12. Given an array arr[], find the maximum j – i such that arr[j] > arr[i]

a = []

arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
for i in range(len(arr)):
    for j in range(len(arr)-1,-1,-1):
        if arr[j] > arr[i]:
            a.append(j-i)
max(a)