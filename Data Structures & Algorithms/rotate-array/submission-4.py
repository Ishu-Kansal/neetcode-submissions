class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        tmp = nums[(len(nums)-k):]
        print(tmp)

        for i in range(len(nums)-1, k-1, -1):
            nums[i] = nums[i-k]
        for j in range(k):
            nums[j] = tmp[j]