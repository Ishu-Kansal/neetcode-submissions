# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       
        def compareHeights(currNode):
            if(currNode is None):
                return [True, 0]
            leftHeights = compareHeights(currNode.left)
            rightHeights = compareHeights(currNode.right)
            balanced = leftHeights[0] and rightHeights[0] and (abs(leftHeights[1]-rightHeights[1]) <= 1)
            return [balanced, 1 + max(leftHeights[1], rightHeights[1])]
        
        return compareHeights(root)[0]
            
            