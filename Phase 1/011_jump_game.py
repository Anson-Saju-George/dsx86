def can_jump(nums):
    farthest = 0

    for i, jump in enumerate(nums):
        if i > farthest:  # can't even reach index i
            return False
        farthest = max(farthest, i + jump)
        print(i, "", jump)

    return True


# Example usage:
#              [0, 1, 2, 3, 4]
print(can_jump([2, 3, 1, 1, 4]))  # True
print(can_jump([3, 2, 1, 0, 4]))  # False
