"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda inter: inter.start)
        endpoints = []
        heapq.heapify(endpoints)
        maxRooms = 0

        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            while(endpoints and endpoints[0] <= start):
                heapq.heappop(endpoints)
            heapq.heappush(endpoints, end)
            maxRooms = max(maxRooms, len(endpoints))

        return maxRooms
            

