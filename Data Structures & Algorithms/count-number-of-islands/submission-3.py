class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        explore_stack = []
        seen = set()
        totalIslands = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in seen:
                    explore_stack.append((i, j))
                    seen.add((i, j))
                    totalIslands += 1
                    
                    while explore_stack:
                        r, c = explore_stack.pop()
                        
                        if r + 1 < n and grid[r + 1][c] == "1" and (r + 1, c) not in seen:
                            explore_stack.append((r + 1, c))
                            seen.add((r + 1, c))
                        if r - 1 >= 0 and grid[r - 1][c] == "1" and (r - 1, c) not in seen:
                            explore_stack.append((r - 1, c))
                            seen.add((r - 1, c))
                        if c + 1 < m and grid[r][c + 1] == "1" and (r, c + 1) not in seen:
                            explore_stack.append((r, c + 1))
                            seen.add((r, c + 1))
                        if c - 1 >= 0 and grid[r][c - 1] == "1" and (r, c - 1) not in seen:
                            explore_stack.append((r, c - 1))
                            seen.add((r, c - 1))
                            
        return totalIslands