# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(first, second) -> bool:
            stack = []
            stack.append((first, second))
            while(len(stack) > 0):
                node1, node2 = stack.pop()
                if(node1 is None and node2 is None):
                    continue
                if(node1 is None or node2 is None or node1.val != node2.val):
                    return False
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))

            return True
        
        if(root is None and subRoot is None):
            return True
        
        if(isSameTree(root, subRoot)):
            return True
        if(root is None and subRoot is not None or (root is not None and subRoot is None)):
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)