class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        if(len(edges) == 0 and n == 1):
            return True
        queue = collections.deque()

        adjMat = [[] for _ in range(n)]

        for edge in edges:
            start, end = edge
            adjMat[start].append(end)
            adjMat[end].append(start)
        for initial in adjMat[edges[0][0]]:
            queue.append((initial, edges[0][0]))
        visited.add(edges[0][0])
        print(adjMat)
        while(len(queue) > 0):
            print(queue)
            currNode, origin = queue.popleft()
            visited.add(currNode)
            for node in adjMat[currNode]:
                if(node != origin):
                    queue.append((node, currNode))
                    
                    if(node in visited):
                        return False
                    else:
                        visited.add(node)
        print(len(visited))
        if(len(visited) < n):
            return False
        
        return True




