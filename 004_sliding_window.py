"""
    Two Pointer / Sliding Window Algorithms
    Finding the longest substring without repeating characters
"""


def length_of_longest_substring(s: str) -> int:
    last_seen = {} # character -> last seen index
    left = 0 # left pointer of the sliding window
    max_len = 0 # maximum length of substring without repeating characters

    for right, ch in enumerate(s): # right pointer of the sliding window
        if ch in last_seen and last_seen[ch] >= left: # character already seen in the current window
            left = last_seen[ch] + 1

        last_seen[ch] = right
        max_len = max(max_len, right - left + 1)

    return max_len


def longest_substring(s: str):
    last_seen = {}
    left = 0
    max_len = 0
    start = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1

        last_seen[ch] = right

        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left

    return s[start : start + max_len], max_len


if __name__ == "__main__":
    s = "wdoawudwdiuhaihwddiw"
    sub, ln = longest_substring(s)
    print("Input      :", s)
    print("Substring  :", sub)
    print("Length     :", ln)


if __name__ == "__main__":
    print(length_of_longest_substring("wdoawudwdiuhaihwddiw"))
