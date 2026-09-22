class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            counter = target - nums[i]
            if(counter in indices):
                return [indices[counter], i]
            indices[nums[i]] = i
        return []
         
