# Maximum Non-Overlapping Intervals


def max_non_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by end time
    count = 0
    last_end = float("-inf")

    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end

    return count


def select_non_overlapping_intervals(intervals):
    # sort by end time
    intervals = sorted(intervals, key=lambda x: x[1])

    selected = []
    last_end = float("-inf")

    for start, end in intervals:
        if start >= last_end:
            selected.append([start, end])  # we choose this interval
            last_end = end  # update boundary

    return selected


intervals = [(1, 3), (2, 4), (3, 5), (6, 7), (5, 8)]
result = max_non_overlapping_intervals(intervals)
print("Input Intervals       :", intervals)
print("Max Non-Overlapping Intervals Count :", result)
selected_intervals = select_non_overlapping_intervals(intervals)
print("Selected Non-Overlapping Intervals  :", selected_intervals)
