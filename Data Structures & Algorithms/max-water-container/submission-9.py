class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0
        left = 0
        right = len(heights)-1

        while(left < right):
            
            leftH = heights[left]
            rightH = heights[right]
            currVol = min(leftH, rightH) * (right - left)
            currMax = max(currMax, currVol)

            if(leftH > rightH):
                right -= 1
            else:
                left += 1
        return currMax