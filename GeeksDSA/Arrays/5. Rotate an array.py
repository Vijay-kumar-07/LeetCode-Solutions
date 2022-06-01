arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
def rotate(arr, d):
    a = []
    for i in range(d):
        a.append(arr.pop(0))
    return arr + a
rotate(arr,d)