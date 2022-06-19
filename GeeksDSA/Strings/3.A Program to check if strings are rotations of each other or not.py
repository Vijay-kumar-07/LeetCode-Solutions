s1 = "ABCD"
s2 = "ACBD"

def areRotations(s1, s2):
    if len(s1) != len(s2):
        return False
    temp = s1 + s1
    if temp.count(s2)>0:
        return True
    else:
        return False
areRotations(s1,s2)