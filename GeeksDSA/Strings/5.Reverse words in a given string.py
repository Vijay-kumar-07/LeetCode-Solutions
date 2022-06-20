# 5.Reverse words in a given string

s = "getting good at coding needs a lot of practice"
a = []
split_ = s.split(" ")
for i in range(len(split_)-1,-1,-1):
    a.append(split_[i])
" ".join(a)
 