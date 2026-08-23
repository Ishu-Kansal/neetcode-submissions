# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def isValid(currNode: Optional[TreeNode], validRange: List) -> bool:
            smallest, largest = validRange
            if(currNode is None):
                return True
            if(currNode.val <= smallest):
                return False
            if(currNode.val >= largest):
                return False
            
            return (isValid(currNode.left, [smallest, currNode.val]) and
                    isValid(currNode.right, [currNode.val, largest]))
        
        return isValid(root, [float('-inf'), float('inf')])