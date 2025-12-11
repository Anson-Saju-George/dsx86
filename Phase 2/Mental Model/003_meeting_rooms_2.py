import heapq

def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])  # sort by start
    heap = []  # min-heap of end times
    heapq.heappush(heap, intervals[0][1])

    for s, e in intervals[1:]:
        if s >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, e)
    return len(heap)
