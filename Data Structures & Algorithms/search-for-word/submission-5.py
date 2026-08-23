class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])


        def traverse(ltr, currI, currJ, path) -> bool:
            if(ltr == len(word)):
                return True
            
            if(currI < 0 or currI >= n or currJ < 0 or currJ >= m or 
            word[ltr] != board[currI][currJ] or (currI, currJ) in path):
                return False

            path.add((currI, currJ))
            found = False
            found = found or traverse(ltr+1, currI+1, currJ, path)
            found = found or traverse(ltr+1, currI-1, currJ, path)
            found = found or traverse(ltr+1, currI, currJ+1, path)
            found = found or traverse(ltr+1, currI, currJ-1, path)

            path.remove((currI, currJ))
            return found
        
        for i in range(n):
            for j in range(m):
                path = set()
                isFound = traverse(0, i, j, path)
                if(isFound):
                    return True
        
        return False



