arr = [0,1,2,3]
n,m = 4,5
a = []
for i in range(m):
    if i not in arr:
        a.append(i)
min(a)