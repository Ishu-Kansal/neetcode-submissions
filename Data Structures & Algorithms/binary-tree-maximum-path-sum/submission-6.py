# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxPath = root.val

        def getMaxPath(currNode):
            nonlocal maxPath
            if(currNode is None):
                return
            
            leftLen = getMaxPath(currNode.left)
            rightLen = getMaxPath(currNode.right)

            maxThroughCurr = currNode.val
            maxLeft = currNode.val
            maxRight = currNode.val

            if(leftLen):
                maxThroughCurr += leftLen
                maxLeft += leftLen

            if(rightLen):
                maxThroughCurr += rightLen
                maxRight += rightLen

            maxPath = max(maxPath, maxLeft, maxRight, maxThroughCurr, currNode.val)

            return max(maxLeft, maxRight, currNode.val)
        
        getMaxPath(root)

        return maxPath