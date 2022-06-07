# 15. Find the two numbers with odd occurrences in an unsorted array

arr = [10, 20]
a = []
for i in arr:
    cnt_ = arr.count(i)
    if cnt_ % 2 != 0:
        a.append(i)
print(f"{a[0]} and {a[1]}" )