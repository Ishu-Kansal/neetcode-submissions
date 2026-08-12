# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(newRoot):
            if newRoot is None:
                return newRoot
            temp = newRoot.left
            newRoot.left = invert(newRoot.right)
            newRoot.right = invert(temp)
            return newRoot
        
        invert(root)


        return root
