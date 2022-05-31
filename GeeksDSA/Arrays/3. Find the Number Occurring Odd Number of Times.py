arr = [5,7,2,7,5,2,5]
ans = []
output = 0
for i in arr:
    ans.append(arr.count(i))
for j in ans:
    if j%2 != 0:
        output = j
index_ = ans.index(output)
arr[index_]

# bitwise XOR of all the elements. 

res = 0
for i in arr:
    res = res ^ i
res