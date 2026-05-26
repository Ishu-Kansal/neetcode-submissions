class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxVal = max(nums)
        minVal = min(nums)

        counts = {}

        for num in nums:
            if(num in counts):
                counts[num] += 1
            else:
                counts[num] = 1
        
        countBuckets = [[] for i in range(len(nums) + 1)]

        for key, val in counts.items():
            countBuckets[val].append(key)

        left = k
        retArr = []

        for i in range(len(countBuckets)-1, -1, -1):
            if(left > 0 and countBuckets[i] is not None):
                for num in (countBuckets[i]):
                    retArr.append(num)
                    left -= 1
                    if(left <= 0):
                        return retArr
            else:
                return retArr
        return retArr
