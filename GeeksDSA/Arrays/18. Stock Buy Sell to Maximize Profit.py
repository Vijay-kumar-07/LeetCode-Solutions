# 18. Stock Buy Sell to Maximize Profit

arr = [100, 180, 260, 310, 40, 535, 695]

def maximize_profit(arr):
    min_index = arr.index(min(arr))
    max_1 = arr[0:min_index]
    profit1 = max(max_1) - min(max_1)
    max_2 = arr[min_index:]
    profit2 = max(max_2) - min(max_2)
    return profit1 + profit2
maximize_profit(arr)