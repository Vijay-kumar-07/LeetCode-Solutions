# 167. Two Sum II - Input Array Is Sorted

numbers = [-1,0]
target = -1
a = []
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            a.append(i+1)
            a.append(j+1)
a        