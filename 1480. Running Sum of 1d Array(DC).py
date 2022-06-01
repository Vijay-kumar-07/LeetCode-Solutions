nums = [3,1,2,10,1]
a,s =[],nums[0]
for i in range(1,len(nums)):
    a.append(s)
    s += nums[i]
a.append(s)
a