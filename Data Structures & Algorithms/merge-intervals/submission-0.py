class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals = sorted(intervals, key=lambda interval: interval[0])

        i = 0
        while(i < len(intervals)):
            start_i = intervals[i][0]
            end_i = intervals[i][1]
            
            i += 1
            while(True):
                if(i >= len(intervals)):
                    res.append([start_i, end_i])
                    break
                currInterval = intervals[i]
                if(currInterval[0] >= start_i and currInterval[0] <= end_i):
                    end_i = max(end_i, currInterval[1])
                    i += 1
                else:
                    res.append([start_i, end_i])
                    break
        
        return res