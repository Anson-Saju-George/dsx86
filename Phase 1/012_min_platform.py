def min_platforms(arrivals, departures):
    arrivals.sort()  # Sort arrival times
    departures.sort()  # Sort departure times

    i = j = 0
    platforms = 0
    max_platforms = 0
    n = len(arrivals)

    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            # train arrives before next departs → need one more platform
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            # a train departs before next arrives → free one platform
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

# 🔎 First, list arrivals and departures:

# Arrivals = [9, 9.5]
# Departures = [11, 12]

# ✔️ Final Answer: 2 platforms required

# Makes sense:

# Train B: 9–12
# Train A: 9.5–11

# They overlap, so two trains are at station at the same time → need 2 platforms.

# 🧠 Why this case works correctly with sorting

# Because we never say:

# “Train arriving at 9 belongs to departure at 11”

# We say:

# “At time 9 → one platform needed
# At time 9.5 → another platform needed
# At time 11 → one leaves
# At time 12 → second one leaves”

# This reasoning is time-based, not identity-based.
