class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSums = [nums[0]]

        for i in range(1, len(nums)):
            currMax = max(maxSums[i-1] + nums[i], nums[i])
            maxSums.append(currMax)
        
        total = nums[0]
        for i in range(len(maxSums)):
            if(maxSums[i] > total):
                total = maxSums[i]
        
        return total