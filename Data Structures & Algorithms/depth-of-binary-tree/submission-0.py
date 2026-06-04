# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0
        if(root.left is None and root.right is None):
            return 1
        leftDepth = 0
        rightDepth = 0
        if(root.left is not None):
            leftDepth = self.maxDepth(root.left)
        if(root.right is not None):
            rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)
        