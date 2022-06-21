str1 = "LISTEN"
str2 = "SILENT"

def anagram(str1, str2):
    for i in str1:
        if i not in str2:
            return 1
    return 0
if anagram(str1, str2):
    print("Not Anagram")
else:
    print("Two strings are Anagram")