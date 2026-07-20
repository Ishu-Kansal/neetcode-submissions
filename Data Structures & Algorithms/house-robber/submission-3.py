class Solution:
    def rob(self, nums: List[int]) -> int:

        if(len(nums) <= 2):
            return max(nums)
        if(len(nums) == 3):
            return max(nums[0] + nums[2], nums[1])

        cumsum = [nums[0], max(nums[0], nums[1])]
        cumsum.append(max(nums[0] + nums[2], nums[1]))

        for i in range(3, len(nums)):
            threeBefore = nums[i] + cumsum[i-3]
            twoBefore = nums[i] + cumsum[i-2]
            skip = cumsum[i-1]
            cumsum.append(max(threeBefore, twoBefore, skip))
        
        return cumsum[-1]
