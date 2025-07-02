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

def Threesum(nums):
    nums.sort()
    i=0
    n=len(nums)
    Sum=0
    result=[]
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]: continue # to avoid duplicates
        k=n-1
        j=i+1
        while j<k:
            Sum=nums[i]+nums[j]+nums[k]
            if Sum==0:
               result.append([nums[i],nums[j],nums[k]])
               while nums[j]==nums[j+1] and j<k: j+=1   # to avoid duplicates
               while nums[k]==nums[k-1] and j<k: k-=1   # to avoid duplicates
               j+=1
               k-=1
            if Sum>0:
                k=k-1
            else:
                j=j+1
    return result
nums=[-1,1,0,0,-1,1,1,1]
print(Threesum(nums))           
# thought was going from input to output but my mind is thinking the opposite way, its really simple, keep things simple and we'll get the output,
# just think and code, you'll get the output, just keep coding.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return None
        k=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k+=1
        return k
# where did I go wrong? this question was easy only if I give more time to analyzr question mindfully, just needed to update the slow pointer here nothing else
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        if n < 3:
            return 0  # Assuming n >= 3 per problem constraints
        min_diff = float('inf')
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                diff = abs(current_sum - target)
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = current_sum
                if current_sum == target:
                    return current_sum
                elif current_sum > target:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return closest_sum
    
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        n=len(nums)
        if n==0:
            return
        if n==1:
            return nums
        while j<n:
            if nums[j]==0:
                j+=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
        return nums
        
class Solution(object):
    def findUnsortedSubarray(self, nums):
        if len(nums)<2:
            return 0
        start=0
        n=len(nums)
        end=n-1
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                start=i
                break
        else:
                return 0
        for i in range(n-1,0,-1):
            if nums[i]<nums[i-1]:
                end=i
                break
        max_val=max(nums[start:end+1])
        min_val=min(nums[start:end+1])
        while start>0 and nums[start-1]>min_val:
            start-=1
        while end<n-1 and nums[end+1]<max_val:
            end+=1
        return end-start+1
#We did good tho the problem was the last step where while loop extends the sub array by taking min and max value, Good Job we'll do it later