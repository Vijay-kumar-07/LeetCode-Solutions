string = "function"
def myAtoi(string):
    res = 0
    for i in range(len(string)):
        res = res * 10 + (ord(string[i]) - ord('0'))
    return res
myAtoi(string)