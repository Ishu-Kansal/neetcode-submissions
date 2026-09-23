class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sums = set()
        for i in range(len(nums)-2):
                j = i + 1
                k = len(nums)-1
                target = 0 - nums[i]
                while(j < k):
                    if(nums[j] + nums[k] < target):
                        j += 1
                    elif(nums[j] + nums[k] > target):
                        k -= 1
                    else:
                        sums.add((nums[i], nums[j],nums[k]))
                        j += 1

        return list(sums)