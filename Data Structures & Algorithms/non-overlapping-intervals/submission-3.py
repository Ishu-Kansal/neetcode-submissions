class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        def isIntersecting(a, b) -> bool:
            if(b[0] < a[1]):
                return True
            return False

        if(len(intervals) <= 1):
            return 0

        intervals = sorted(intervals, key=lambda interval: interval[1])
        newIntervals = []
        i = 1
        j = 0

        while(i < len(intervals) and j < len(intervals)):
            newIntervals.append(intervals[j])
            while(i < len(intervals) and isIntersecting(intervals[j], intervals[i])):
                i += 1
            j = i
        return len(intervals) - len(newIntervals)