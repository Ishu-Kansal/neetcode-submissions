class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        totalCounted = 0
        minI = 0
        maxI = len(matrix)
        minJ = 0
        maxJ = len(matrix[0])
        path = []
        while(True):
            if(totalCounted >= len(matrix)* len(matrix[0])):
                break
            # right
            for j in range(minJ, maxJ):
                path.append(matrix[minI][j])
                totalCounted += 1
            minI += 1
            if(totalCounted >= len(matrix)* len(matrix[0])):
                break
            # down
            for i in range(minI, maxI):
                path.append( matrix[i][maxJ-1])
                totalCounted += 1
            maxJ -= 1
            if(totalCounted >= len(matrix)* len(matrix[0])):
                break
            # left
            for j in range(maxJ-1, minJ - 1, -1):
                path.append(matrix[maxI - 1][j])
                totalCounted += 1
            maxI -= 1
            if(totalCounted >= len(matrix)* len(matrix[0])):
                break
            # up
            for i in range(maxI-1, minI-1, -1):
                path.append(matrix[i][minJ])
                totalCounted += 1
            minJ += 1
        return path






