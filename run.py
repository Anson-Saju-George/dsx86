def longest_substring_bruteforce(s: str) -> int:
    max_length = 0
    n = len(s)
    
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_length = max(max_length, j - i + 1)
    
    return max_length






print(longest_substring_bruteforce("abcabcbb"))  # 3
print(longest_substring_bruteforce("bbbbb"))  # 1
print(longest_substring_bruteforce("pwwkew"))  # 3

