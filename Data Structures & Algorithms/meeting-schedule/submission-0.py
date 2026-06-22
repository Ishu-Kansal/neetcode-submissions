"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedIntervals = sorted(intervals, key=lambda inter: inter.start)

        for i in range(1, len(sortedIntervals)):
            if(sortedIntervals[i-1].end > sortedIntervals[i].start):
                return False
        
        return True