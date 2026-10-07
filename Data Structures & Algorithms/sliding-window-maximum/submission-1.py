class Solution:
    from sortedcontainers import SortedList
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = self.SortedList([])


        for i in range(k):
            heap.add(nums[i])
        
        ret = [heap[-1]]
        i = k
        while(i < len(nums)):
            heap.add(nums[i])
            heap.remove(nums[i-k])
            ret.append(heap[-1])
            i += 1

        return ret