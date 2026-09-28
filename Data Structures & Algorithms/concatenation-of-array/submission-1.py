class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        retArr = [0] * (2 * len(nums))
        n = len(nums)
        for i in range(n):
            retArr[i] = nums[i]
            retArr[n+i] = nums[i]
        return retArr 