class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0

        numZeros = 0

        while(j < len(nums)):
            if(nums[j] != 0):
                nums[i] = nums[j]
                i += 1
            else:
                numZeros += 1
            j += 1
        
        print(numZeros)
        for zero in range(len(nums)-numZeros, len(nums)):
            nums[zero] = 0

        
        return nums
        