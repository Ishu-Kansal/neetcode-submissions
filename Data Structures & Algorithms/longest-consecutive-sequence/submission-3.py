class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxFreq = 0

        while(len(numSet) > 0):
            base = next(iter(numSet))
            numSet.remove(base)
            currFreq = 1
            travPos = base + 1
            while(travPos in numSet):
                print(travPos)
                numSet.remove(travPos)
                currFreq += 1
                travPos += 1
            travNeg = base - 1
            while(travNeg in numSet):
                print(travNeg)
                numSet.remove(travNeg)
                currFreq += 1
                travNeg -= 1
            maxFreq = max(maxFreq, currFreq)

        return maxFreq
