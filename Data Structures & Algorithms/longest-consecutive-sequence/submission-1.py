class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)== 0 or len(nums) == 1):
            return len(nums)
        maxVal = max(nums)
        minVal = min(nums)
        counts = [0] * (maxVal - minVal + 1)

        for num in nums:
            counts[num-minVal] += 1
        
        maxLen = 0
        currLen = 0
        for count in counts:
            if(count > 0):
                currLen+= 1
                maxLen = max(maxLen, currLen)
            else:
                currLen = 0

        return maxLen

