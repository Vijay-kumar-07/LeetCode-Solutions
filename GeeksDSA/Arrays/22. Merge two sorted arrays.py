a1 = [10]
a2 = [2,3]
n1,n2 = len(a1), len(a2)
merged = a1 + a2
sorted_ = sorted(merged)
a1 = sorted_[:n1]
a2 = sorted_[n1:]
a1,a2