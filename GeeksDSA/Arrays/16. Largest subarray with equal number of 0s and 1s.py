# Largest subarray with equal number of 0s and 1s

from iteration_utilities import first
from itertools import chain

arr = [1, 1,1,1]
s = set()

def largest_subarray(arr):
    for i in arr:
        s.add(arr.count(i))
    first_ = first(s)
    for j in range(len(arr)):
        a = []
        a.append(arr[j:])
        a = list(chain.from_iterable(a))
        if a.count(0) == a.count(1):
            if a.count(0) == first_:
                print(f"{j} to {len(a)}")
                return 1
    return 0
if (largest_subarray(arr)):
    print("")
else:
    print("No such subarray")