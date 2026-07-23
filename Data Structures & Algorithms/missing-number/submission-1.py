class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)+1
        totalSumTarget = int((n * (n-1))/2)
        totalCurr = 0
        for num in nums:
            totalCurr += num
        if(totalSumTarget == totalCurr):
            return 0
        
        return (totalSumTarget - totalCurr)
