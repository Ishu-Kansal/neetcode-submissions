class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def getDirections(a, b):
            ret = []
            if(a-1 >= 0 and grid[a-1][b] == "1"):
                ret.append((a-1, b))
            if(a + 1 < len(grid) and grid[a+1][b] == "1"):
                ret.append((a+1, b))
            if(b-1 >= 0 and grid[a][b-1] == "1"):
                ret.append((a, b-1))
            if(b + 1 < len(grid[0]) and grid[a][b+1] == "1"):
                ret.append((a, b+1))
            return ret

        def dfs(i, j):
            toCheck = [(i, j)]
            while(len(toCheck) > 0):
                curr = toCheck.pop()
                grid[curr[0]][curr[1]] = 0
                toCheck += getDirections(curr[0], curr[1])


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if(grid[r][c] == "1"):
                    
                    dfs(r, c)
                    count += 1

        return count



