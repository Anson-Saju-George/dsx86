
def can_jump(nums):
    farthest = 0

    for i, jump in enumerate(nums):
        if i > farthest:        # can't even reach index i
            return False
        farthest = max(farthest, i + jump)

    return True

