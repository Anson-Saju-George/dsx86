# Longest Substring Without Repeating Characters - Brute Force Approach


def longest_substring_bruteforce(s: str) -> int:
    n = len(s)
    max_len = 0

    for i in range(n):
        seen = set()  # Initialize a set to track seen characters
        for j in range(i, n):  # Iterate over the substring starting at index i
            if s[j] in seen:  # If character is already seen, break the loop
                break
            seen.add(s[j])  # Add character to the set if not seen
            max_len = max(max_len, j - i + 1
            )  # Update max_len if current substring is longer

    return max_len  # Return the length of the longest substring without repeating characters


print(longest_substring_bruteforce("abcabcbb"))  # 3
print(longest_substring_bruteforce("bbbbb"))  # 1
print(longest_substring_bruteforce("pwwkew"))  # 3
