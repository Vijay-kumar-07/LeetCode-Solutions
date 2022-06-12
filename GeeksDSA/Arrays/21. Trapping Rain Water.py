arr = [3,0,2,0,4]
n = len(arr)
def maxWater(arr,n):
    res = 0
    for i in range(1, n-1):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
        right = arr[i]
        for j in range(i+1,n):
            right = max(right, arr[j])
        res = res + (min(left, right) - arr[i])
    return res
    
maxWater(arr, n)