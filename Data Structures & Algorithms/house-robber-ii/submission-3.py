class Solution:
    def rob(self, nums: List[int]) -> int:
        firstPass = nums[1:]
        secondPass = nums[:len(nums)-1]

        if(len(nums) <= 2):
            return max(nums)

        dp1 = [0, nums[1]] # pad zero at front
        dp2 = [nums[0], max(nums[0], nums[1])] # pad zero at back

        currMax = nums[0]

        for i in range(2, len(nums)):
            cM = max(dp1[i-2] + nums[i], dp1[i-1])
            dp1.append(cM)
            currMax = max(currMax, cM)

        for i in range(2, len(nums)-1):
            cM = max(dp2[i-2] + nums[i], dp2[i-1])
            dp2.append(cM)
            currMax = max(currMax, cM)

        return currMax
        

