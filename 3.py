
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])  # sort by end
    non_overlap = 1
    last_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= last_end:
            non_overlap += 1
            last_end = end
        # else: this one overlaps → we "remove" it logically

    return len(intervals) - non_overlap


