def min_platforms(arrivals, departures):
    arrivals.sort()  # Sort arrival times
    departures.sort()  # Sort departure times

    i = j = 0
    platforms = 0
    max_platforms = 0
    l = len(arrivals)

    while i < l and j < l:
        if arrivals[i] <= departures[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return max_platforms


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

# Example usage:
print(min_platforms(arr, dep))  # Output: 3
print(min_platforms([100, 200, 300], [150, 250, 350]))  # Output: 1
print(min_platforms([100, 200, 300], [120, 220, 320]))  # Output: 1
print(min_platforms([900, 950], [1100, 1200]))  # Output: 2
