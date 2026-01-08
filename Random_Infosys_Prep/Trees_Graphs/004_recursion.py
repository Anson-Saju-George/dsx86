"""Count Occurrences"""
def count_occurrences(arr, x):
    if not arr:
        return 0
    return (1 if arr[0] == x else 0) + count_occurrences(arr[1:], x)

# Example
arr = [1, 2, 2, 3, 2]
x = 2
print(count_occurrences(arr, x))  # 3

"""Sorted"""
def is_sorted(arr, i=0):
    if i >= len(arr) - 1:
        return True
    if arr[i] > arr[i + 1]:
        return False
    return is_sorted(arr, i + 1)

# Examples
print(is_sorted([1, 2, 3, 4]))  # True
print(is_sorted([1, 3, 2]))     # False

"""First, Last, All Indices"""

def first_index(arr, x, i=0):
    if i == len(arr):
        return -1
    if arr[i] == x:
        return i
    return first_index(arr, x, i + 1)

# Example
print(first_index([1, 2, 3, 2, 4], 2))  # 1


def last_index(arr, x, i=0):
    if i == len(arr):
        return -1

    idx = last_index(arr, x, i + 1)

    if idx != -1:
        return idx
    if arr[i] == x:
        return i
    return -1


# Example
print(last_index([1, 2, 3, 2, 4], 2))  # 3


def all_indices(arr, x, i=0):
    if i == len(arr):
        return []

    rest = all_indices(arr, x, i + 1)

    if arr[i] == x:
        return [i] + rest
    return rest

# Example
print(all_indices([1, 2, 3, 2, 4], 2))  # [1, 3]

"""Subsequences"""
def subsequences(s):
    if not s:
        return [""]

    rest = subsequences(s[1:])
    res = []

    for sub in rest:
        res.append(sub)          # exclude current char
        res.append(s[0] + sub)   # include current char

    return res


# Example
print(subsequences("ab"))
# ["", "b", "a", "ab"]

"""Balanced Parentheses"""
def is_balanced(s, i=0, bal=0):
    if bal < 0:
        return False          # more ')' than '(' at some point
    if i == len(s):
        return bal == 0       # all opened must be closed

    if s[i] == '(':
        return is_balanced(s, i + 1, bal + 1)
    else:  # ')'
        return is_balanced(s, i + 1, bal - 1)


# Examples
print(is_balanced("((()))"))  # True
print(is_balanced("(()"))     # False
print(is_balanced("())("))    # False

"""Remove Consecutive Duplicates"""
def remove_consecutive(s):
    if len(s) <= 1:
        return s

    rest = remove_consecutive(s[1:])

    if s[0] == rest[0]:
        return rest
    return s[0] + rest


# Example
print(remove_consecutive("aabbcca"))  # "abca"
