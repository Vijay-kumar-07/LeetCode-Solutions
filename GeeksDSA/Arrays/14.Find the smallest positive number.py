# 14. Find the smallest positive number missing from an unsorted array 

arr = [2, 3, 7, 6, 8, -1, -10, 15]

a = []
for i in range(1, len(arr)):
    if i not in arr:
        a.append(i)
min(a)

# November 25 2022
def smallestmissing(arr):
    arr.sort()
    if max(arr) < 1:
        return 1
    if max(arr) == 1:
        return 2
    for i in range(1, max(arr)):
        if i not in arr:
            return i
            break
    
if __name__ =='__main__':
    arr = [2, 3, -7, 6, 8, 1, -10, 15]
    print(smallestmissing(arr))
