# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        overall = []
        currK = k
        smallest = root.val

        def traverse(currNode):
            nonlocal currK, smallest
            if(currNode is None):
                return None
            
            traverse(currNode.left)
            if(currK == 0):
                return
            currK -= 1
            if(currK == 0):
                smallest = currNode.val
                return
            traverse(currNode.right)



        traverse(root)
        return smallest
