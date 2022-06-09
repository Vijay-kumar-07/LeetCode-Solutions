# 19. Find common elements in three sorted arrays

a1 = [1, 5, 10, 20, 40, 80]
a2 = [6, 7, 20, 80, 100]
a3 = [3, 4, 15, 20, 30, 70, 80, 120]

for i in a1:
    for j in a2:
        for k in a3:
            if i == j == k:
                print(i, end = " ")
            else:
                pass