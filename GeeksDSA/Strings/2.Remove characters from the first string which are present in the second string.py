mask_string = "mask"
string = "geeksforgeeks"

for i in mask_string:
    if i in string:
        string = string.replace(i,"")
string