# 20. Nuts & Bolts Problem (Lock & Key problem) 

nuts = ['@', '#', '$', '%', '^', '&']
Bolts = ['$', '%', '&', '^', '@', '#']

b,n = [],[]
for i in Bolts:
    for j in nuts:
        if i == j:
            b.append(i)
            n.append(j)
for i in b:
    print(i, end = " ")
print("\n")
for j in n:
    print(j, end = " ")