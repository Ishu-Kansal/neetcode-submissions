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
                return 0
            
            leftLen = max(getMaxPath(currNode.left), 0)
            rightLen = max(getMaxPath(currNode.right), 0)


            maxPath = max(maxPath, leftLen + currNode.val + rightLen, leftLen + currNode.val, rightLen + currNode.val)

            return currNode.val + max(leftLen, rightLen)
        
        getMaxPath(root)

        return maxPath