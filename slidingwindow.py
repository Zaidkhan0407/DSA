def length_of_longest_substring_k_distinct(s, k):
    count = {}
    max_len = 0
    i = 0
    for j in range(len(s)):
        if s[j] in count:
            count[s[j]] += 1
        else:
            count[s[j]] = 1
        
        while len(count) > k:
            count[s[i]] -= 1
            if count[s[i]] == 0:
                del count[s[i]]
            i += 1
        max_len = max(max_len, j - i + 1)
    return max_len

s = "eceba"
k = 2
print(length_of_longest_substring_k_distinct(s, k))

def maxsubarr(nums, target):
    if not nums:
        return 0
    n=len(nums)
    i=0
    curr_sum=0
    min_len=float("inf")
    for j in range(n):
        curr_sum+=nums[j]
        while curr_sum>=target:
            min_len=min(min_len,j-i+1)
            curr_sum-=nums[i]
            i+=1
    return min_len if min_len !=float("inf") else 0

nums=[2, 3, 1, 2, 7, 3]
print(maxsubarr(nums, 7))