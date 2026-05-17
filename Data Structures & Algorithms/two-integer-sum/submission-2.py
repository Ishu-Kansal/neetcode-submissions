class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap = {} # map VAL to IDX
        for i in range(len(nums)):
            if((target-nums[i] in idxMap)): 
                return [idxMap[target-nums[i]], i]
            else:
                idxMap[nums[i]] = i
