def longest_substring(s: str):
    ls = {}
    l = 0
    max_len = 0
    
    for r , ch in enumerate(s):
        if ch in ls and ls[ch] >= l:
            l = ls[ch] + 1
        
        ls[ch] = r
        max_len = max(max_len, r - l + 1)

    return max_len


s = "wdoawudwdiuhaihwddiw"
print(longest_substring(s))