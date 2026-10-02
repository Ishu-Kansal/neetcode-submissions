class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        greatestCount = 0
        greatest = None
 
        for key, val in counts.items():
            if(val > greatestCount):
                greatest = key
                greatestCount = val
        
        return greatest