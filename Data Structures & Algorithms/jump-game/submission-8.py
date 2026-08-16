class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0

        while(pos < len(nums)-1 ):
            if(nums[pos] == 0 and pos != len(nums)-1):
                return False
            
            maxIdxToJumpTo = nums[pos] + pos
            atIndex = pos
            
            for i in range(pos, nums[pos]+pos+1):
                if(i >= len(nums)-1):
                    return True
                if(nums[i] + i > maxIdxToJumpTo):
                    maxIdxToJumpTo = nums[i] + i
                    atIndex = i
            print("can jump to ", maxIdxToJumpTo)
            if(maxIdxToJumpTo >= len(nums)-1):
                return True
            if(atIndex == pos):
                return False
            print("jumping to ", atIndex)
            pos = atIndex
            print('\n')

        return True