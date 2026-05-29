class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMultiply = [1]
        rightMultiply = [1]

        for i in range(1, len(nums)):
            leftMultiply.append(leftMultiply[i-1] * (nums[i-1]))
        
        for j in range(len(nums)-2, -1, -1):
            rightMultiply.append(rightMultiply[len(nums)-j-2] * (nums[j+1]))

        rightMultiply = rightMultiply[::-1]

        answer = []


        for k in range(len(leftMultiply)):
            answer.append(leftMultiply[k] * rightMultiply[k])
        return answer