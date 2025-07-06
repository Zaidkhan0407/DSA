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