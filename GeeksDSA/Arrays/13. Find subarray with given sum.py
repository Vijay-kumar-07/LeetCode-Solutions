# 13. Find subarray with given sum | Set 1 (Nonnegative Numbers)

arr = [1, 4] 
sum_ =0


def find_subarray(arr, sum_):
    for i in range(len(arr)):
        s = 0
        s += arr[i]
        for j in range(i+1, len(arr)):
            s += arr[j]
            if s == sum_:
                print(f"Sum found between indexes {i} and {j}")
                return 1
    return 0
if find_subarray(arr, sum_):
    print("")
else:
    print("No subarray found")