# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if(p.val > q.val):
            temp = p
            p = q
            q = temp

        lcm = root


        def traverse(currNode):
            nonlocal lcm
            print("traversing ", currNode.val)
            if(p.val == currNode.val or q.val == currNode.val):
                lcm = currNode
                return
            if(p.val < currNode.val and q.val > currNode.val):
                lcm = currNode
                return
            
            if(p.val < currNode.val and q.val < currNode.val):
                traverse(currNode.left)
            if(p.val > currNode.val and q.val > currNode.val):
                traverse(currNode.right)

        traverse(root)
        return lcm