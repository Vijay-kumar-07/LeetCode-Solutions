arr = [16,17,4,3,5,2]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] <= arr[j]:
            break
    if j == len(arr)-1:
        print(arr[i],end = " ")