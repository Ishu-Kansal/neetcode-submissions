# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        currMax = 0

        # returns max length of path in descendent, updates max path through node
        def maxLen(currNode):
            nonlocal currMax
            if currNode is None:
                return 0
            if(currNode.left is None and currNode.right is None):
                return 1
            rightLen = maxLen(currNode.right)
            leftLen = maxLen(currNode.left)
            currMax = max(currMax, rightLen + leftLen)
            return max(rightLen, leftLen) + 1
        
        maxLen(root)
        return currMax