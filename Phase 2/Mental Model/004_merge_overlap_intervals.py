def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged


print(merge_intervals([[1, 3], [2, 4], [5, 7], [6, 8]]))  # [[1, 4], [5, 8]]
print(merge_intervals([[1, 5], [6, 10], [11, 15]]))  # [[1, 5], [6, 10], [11, 15]]
print(merge_intervals([[1, 4], [2, 3]]))  # [[1, 4]]
