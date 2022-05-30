arr =[3,3,4,2,4,4,2,4]
def majority(arr):
    n = len(arr)//2
    cnt_ = []
    for i in arr:
        cnt_.append(arr.count(i))
    max_index = cnt_.index(max(cnt_))
    if max(cnt_) > n:
        return arr[max_index]
    else:
        return "No Majority element"
    
majority(arr)