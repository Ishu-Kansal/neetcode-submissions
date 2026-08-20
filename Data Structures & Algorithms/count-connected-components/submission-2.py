class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = [[] for _ in range(n)]
        nodesToDiscover = set()
        discovered = set()
        for i in range(n):
            nodesToDiscover.add(i)
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            nodes[node1].append(node2)
            nodes[node2].append(node1)
        print(nodes)
        count = 0
        while(len(nodesToDiscover) > 0):
            currNode = next(iter(nodesToDiscover))
            count += 1
            
            stack = [currNode]
            while(len(stack) > 0):
                currNode = stack.pop()
                print("processing node ", currNode)
                nodesToDiscover.remove(currNode)
                discovered.add(currNode)
                adjacencies = nodes[currNode]
                for ex in adjacencies:
                    if(ex not in discovered):
                        stack.append(ex)
                        discovered.add(ex)
                nodes[currNode] = []

        return count
            

