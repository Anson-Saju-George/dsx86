def can_attend_meetings(intervals):
    if not intervals:
        return True

    intervals.sort(key=lambda x: x[0])  # sort by start time

    for i in range(1, len(intervals)):
        prev_end = intervals[i-1][1]
        curr_start = intervals[i][0]

        if curr_start < prev_end:
            return False

    return True

# Example usage:
meetings = [[0, 30], [5, 10], [15, 20]]
meetings2 = [[7, 10], [2, 4]]
print(can_attend_meetings(meetings))  # Output: False
print(can_attend_meetings(meetings2))  # Output: True
