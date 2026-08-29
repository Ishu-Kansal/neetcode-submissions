class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevNeg = 1
        prevPos = 1
        maxProd = nums[0]
        for num in nums:
            currNumMax = prevPos * num
            prevPos = max(num * prevPos, num * prevNeg, num)
            prevNeg = min(currNumMax, num * prevNeg, num)
            maxProd = max(prevPos, maxProd)

        return maxProd 