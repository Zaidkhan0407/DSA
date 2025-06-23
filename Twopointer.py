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

def UniqueSorting(a):
    left=0
    right=1
    while right<len(a):
        if a[left]==a[right]:
            a.pop(right)
        else:
            left=left+1
            right=right+1
    return len(a)
a=[1,1,2]
print(UniqueSorting(a))

def Squareofarr(a):
    left=0
    right=len(a)-1
    temp=a[:]
    n=len(a)
    pos=n-1
    while left<=right:
        if abs(a[left])<abs(a[right]):
            temp[pos]=a[right]**2
            right=right-1
            pos=pos-1
        else:
            temp[pos]=a[left]**2
            left=left+1
            pos=pos-1
    
    return temp
a=[-4,-2,0,3,10]
print(Squareofarr(a))
            
