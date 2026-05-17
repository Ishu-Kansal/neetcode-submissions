class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for i in range(len(nums)):
            if(nums[i] in uniques):
                return True
            uniques.add(nums[i])
        return False