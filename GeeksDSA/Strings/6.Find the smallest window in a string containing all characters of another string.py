# 6.Find the smallest window in a string containing all characters of another string

def smallestWindow(s, p):
    n = len(s)
    if n < len(p):
        return -1
    mp = [0]*256
    start = 0
    ans = n +1
    cnt = 0
    for i in p:
        mp[ord(i)] += 1
        if mp[ord(i)] == 1:
            cnt += 1
            
    j = 0
    i = 0
    while(j < n):
        mp[ord(s[j])] -= 1
        if mp[ord(s[j])] == 0:
            cnt -= 1
            
            while cnt == 0:
                if ans > j - i + 1:
                    ans = j - i + 1
                    start = i
                    
                mp[ord(s[i])] += 1
                if mp[ord(s[i])] > 0:
                    cnt += 1
                i += 1
        j += 1
    if ans > n:
        return "-1"
    return s[start:start+ans]

if __name__ == "__main__":
    string = "this is a test string"
    pattern = "tist"
    result = smallestWindow(string, pattern)
    print(result)