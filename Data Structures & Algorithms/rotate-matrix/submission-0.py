class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(int(len(matrix)/2)):
            firstRow = matrix[i]
            lastRow = matrix[n-i-1]
            matrix[i] = lastRow
            matrix[n - i - 1] = firstRow
        print(matrix)
        for i in range(n):
            for j in range(i, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]  
                matrix[j][i] = tmp