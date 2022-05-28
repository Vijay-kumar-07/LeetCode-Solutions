arr = [1,4, 45,6,10,-8]
x = 16
def sum_(arr,size, x):
    for i in range(size):
        for j in range(1+i, size):
            if arr[j]+arr[i] == x:
                return 1
    return 0

if sum_(arr,len(arr),x):
    print(f"valid pair exists for {x}")
else:
    print(f"No valid pair exists for {x}")