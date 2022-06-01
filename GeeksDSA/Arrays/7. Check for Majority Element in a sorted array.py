arr = [1,1,1,2,2]
x = 1
def majority(arr,x):
    n = len(arr)
    cnt_ = arr.count(x)
    if cnt_ > n/2:
        return True

    return False
majority(arr,x)