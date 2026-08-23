# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        overall = []

        def traverse(level, currNode):
            if(currNode is None):
                return
            while(len(overall) < level + 1):
                overall.append([])
            
            overall[level].append(currNode.val)
            traverse(level+1, currNode.left)
            traverse(level+1, currNode.right)

        traverse(0, root)
        return overall