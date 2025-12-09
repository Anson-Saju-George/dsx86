def find_min_arrow_shots(points):
    if not points:
        return 0

    # sort by end coordinate
    points.sort(key=lambda x: x[1])

    arrows = 1
    curr_end = points[0][1]

    for start, end in points[1:]:
        if start > curr_end:
            arrows += 1
            curr_end = end

    return arrows

# Example usage:
points = [[10,16], [2,8], [1,6], [7,12]]
print(find_min_arrow_shots(points))  # Output: 2


