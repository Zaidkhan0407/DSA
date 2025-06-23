def TwoSum(a,tg):
    left=0
    right=len(a)-1
    while left<right:
        Sum=a[left]+a[right]
        if Sum==tg:
            return left,right
        if tg>Sum:
            left=left+1
        else:
            right=right-1
a=[1,2,3,4,5]
print(TwoSum(a,6))