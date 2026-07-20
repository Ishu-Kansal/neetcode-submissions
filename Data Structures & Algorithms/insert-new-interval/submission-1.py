class Solution:
    
    def isOverlap(self, interval1, interval2):
        if(interval1[1] < interval2[0]):
            return False
        if(interval2[1] < interval1[0]):
            return False
        return True
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newList = []
        i = 0
        while(i < len(intervals) and intervals[i][1] < newInterval[0]):
            newList.append(intervals[i])
            i += 1

        if(i == len(intervals)):
            newList.append(newInterval)
            return newList
        
        while(i < len(intervals) and self.isOverlap(intervals[i], newInterval)):
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        newList.append(newInterval)

        while(i < len(intervals)):
            newList.append(intervals[i])
            i += 1
        return newList




