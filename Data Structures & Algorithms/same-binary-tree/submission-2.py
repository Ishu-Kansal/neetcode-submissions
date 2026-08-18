# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stack = []
        stack.append((p, q))

        while(len(stack) > 0):
            curr = stack[-1]
            stack.pop()
            if(curr[0] is None and curr[1] is None):
                continue
            if(curr[0] is None or curr[1] is None or curr[0].val != curr[1].val):
                return False
            stack.append((curr[0].left, curr[1].left))
            stack.append((curr[0].right, curr[1].right))
        
        return True