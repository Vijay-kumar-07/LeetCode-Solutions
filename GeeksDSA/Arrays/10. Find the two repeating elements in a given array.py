arr = [4,2,4,5,2,3,1]
n = 5
a,b,c= [],[],[]
for i in arr:
    a.append(arr.count(i))
for i in range(len(a)):
    if a[i] == 2:
        b.append(i)
for i in b:
    if arr[i] not in c:
        c.append(arr[i])
for i in range(len(c)):
    print(c[i], end = " ")