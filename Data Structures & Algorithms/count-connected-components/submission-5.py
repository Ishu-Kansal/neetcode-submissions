class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = [[] for _ in range(n)]
        nodesToDiscover = set()
        discovered = set()
        for i in range(n):
            nodesToDiscover.add(i)
        for node1, node2 in edges:
            nodes[node1].append(node2)
            nodes[node2].append(node1)

        count = 0
        while(len(nodesToDiscover) > 0):
            currNode = next(iter(nodesToDiscover))
            count += 1
            
            stack = [currNode]
            while(len(stack) > 0):
                currNode = stack.pop()
                nodesToDiscover.remove(currNode)
                discovered.add(currNode)
                adjacencies = nodes[currNode]
                for ex in adjacencies:
                    if(ex not in discovered):
                        stack.append(ex)
                        discovered.add(ex)
                nodes[currNode] = []

        return count
            

