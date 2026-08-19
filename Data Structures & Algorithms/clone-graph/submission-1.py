"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        explored = {}

        def exploreNode(oldNode) -> Node:
            if(oldNode in explored):
                return
            newNode = Node(oldNode.val, [])
            explored[oldNode] = newNode
            for n in oldNode.neighbors:
                if(n not in explored):
                    newN = exploreNode(n)
                    newNode.neighbors.append(newN)
                else:
                    newNode.neighbors.append(explored[n])
            return newNode
        
        if(node is None):
            return None
        
        newHead = exploreNode(node)
        return newHead


            