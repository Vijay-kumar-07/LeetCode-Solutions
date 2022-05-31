mplusn = [2,8,"NA","NA","NA",13,"NA",15,20]
m = []
n = [5,7,9,25]
for i in mplusn:
    if i != "NA":
        m.append(i)
        
merge = m + n
sorted(merge)