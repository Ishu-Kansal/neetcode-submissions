class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # 5, 6, 7, 8, 1, 2, 3 | search for 6
        while(left < right):
            mid = (left + right) // 2
            if(target == nums[mid]):
                return mid
            if(target == nums[left]):
                return left
            if(target == nums[right]):
                return right
            if(nums[left] < nums[mid]):
                if(nums[left] < target and nums[mid] > target):
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if(nums[mid] < target and nums[right] > target):
                    left = mid + 1
                else:
                    right = mid - 1
        if(nums[left] == target or nums[right] == target):
            return left
        else:
            return -1
            