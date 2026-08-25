class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        sums = []
        for i in range(len(nums)):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            j = i + 1
            k = len(nums)-1
            complement = -1 * nums[i]
            while(j < k):
                if(nums[j] + nums[k] == complement):
                    sums.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while(j < k and nums[j] == nums[j-1]): 
                        j += 1

                if(nums[j] + nums[k] < complement):
                    j += 1
                if(nums[j] + nums[k] > complement):
                    k -= 1
        
        return sums