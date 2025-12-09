
def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()

    i = j = 0
    platforms = 0
    max_platforms = 0
    n = len(arrivals)

    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return max_platforms

