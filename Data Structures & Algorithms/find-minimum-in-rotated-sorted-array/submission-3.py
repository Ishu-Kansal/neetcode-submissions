class Solution:
    def findMin(self, nums: List[int]) -> int:
        firstNum = nums[0]
        left = 0
        right = len(nums)-1
        count = 0
        if(nums[0] <= nums[-1]):
            return nums[0]
        while(left <= right):
            mid = (left + right + 1) // 2
            if(mid == 0):
                return nums[left]
            if(mid == len(nums)-1):
                return nums[right]
            if(nums[mid-1] > nums[mid] and nums[mid+1] > nums[mid]):
                return nums[mid]
            if(nums[mid] <= firstNum):
                right = mid
            elif(nums[mid] > firstNum):
                left = mid
        
        return firstNum