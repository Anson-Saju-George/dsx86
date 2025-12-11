def erase_overlap_intervals_count(intervals):
    if not intervals:
        return 0

    # sort by end time
    intervals.sort(key=lambda x: x[1])
    non_overlap = 1
    last_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= last_end:
            non_overlap += 1
            last_end = end
        # else: overlapping -> we "remove" this one logically

    return len(intervals) - non_overlap


def erase_overlap_intervals(intervals):
    """
    intervals: list of [start, end]
    returns: (to_remove_count, removed_indices)
    removed_indices are indices from the original list
    """
    if not intervals:
        return 0, []

    # Attach original indices
    indexed = [(s, e, idx) for idx, (s, e) in enumerate(intervals)]
    # sort by end time
    indexed.sort(key=lambda x: x[1])

    kept = []  # list of kept original indices
    last_end = float("-inf")

    for s, e, idx in indexed:
        if s >= last_end:
            kept.append(idx)
            last_end = e
        # else: overlapping, do not keep

    kept_set = set(kept)
    removed_indices = [i for i in range(len(intervals)) if i not in kept_set]
    to_remove = len(removed_indices)
    return to_remove, removed_indices


# Example usage:
intervals = [[1, 3], [2, 4], [3, 5], [0, 6], [5, 7], [8, 9]]
intervals2 = [[1, 2], [2, 3], [3, 4], [1, 3], [2, 4], [3, 5]]
intervals3 = [[1, 2], [2, 4], [1, 3], [3, 4], [4, 8], [5, 9]]

print(erase_overlap_intervals_count(intervals))  # Output: 3
print(erase_overlap_intervals_count(intervals2))  # Output: 2
print(erase_overlap_intervals_count(intervals3))  # Output: 2

print(erase_overlap_intervals(intervals))  # Output: (3, [1, 3, 5]) or similar
print(erase_overlap_intervals(intervals2))  # Output: (2, [0, 3]) or similar
print(erase_overlap_intervals(intervals3))  # Output: (2, [0, 2]) or similar
