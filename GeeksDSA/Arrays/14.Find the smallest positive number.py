# 14. Find the smallest positive number missing from an unsorted array 

arr = [2, 3, 7, 6, 8, -1, -10, 15]

a = []
for i in range(1, len(arr)):
    if i not in arr:
        a.append(i)
min(a)