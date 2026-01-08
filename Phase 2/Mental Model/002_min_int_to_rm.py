def min_intervals_to_remove(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])  # sort by end
    count = 0
    last_end = float('-inf')

    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    return len(intervals) - count

# Example usage:
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(min_intervals_to_remove(intervals))  # Output: 1