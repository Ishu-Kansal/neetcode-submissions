# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        overall = []

        def traverse(currNode):
            if(currNode is None):
                return None
            
            traverse(currNode.left)
            overall.append(currNode.val)
            traverse(currNode.right)

        traverse(root)
        print(overall)
        return overall[k-1]
