def min_intervals_to_remove(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])  # sort by end
    count = 0
    last_end = float('-inf')

    for s, e in intervals:
        if s >= last_end:
            count += 1
            last_end = e
    return len(intervals) - count
