class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSums = [nums[0]]
        total = nums[0]
        prev = nums[0]
        for i in range(1, len(nums)):
            currMax = max(prev + nums[i], nums[i])
            prev = currMax
            if(currMax > total):
                total = currMax
        
        return total