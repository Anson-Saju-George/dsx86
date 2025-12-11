def insert_interval(intervals, new):
    res = []
    i = 0
    n = len(intervals)
    ns, ne = new

    # add all intervals ending before new starts
    while i < n and intervals[i][1] < ns:
        res.append(intervals[i])
        i += 1

    # merge overlapping intervals into new
    while i < n and intervals[i][0] <= ne:
        ns = min(ns, intervals[i][0])
        ne = max(ne, intervals[i][1])
        i += 1
    res.append([ns, ne])

    # add remaining intervals
    while i < n:
        res.append(intervals[i])
        i += 1

    return res
