class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        matrix = [[0 for _ in range(len(t))] for _ in range(len(s))]
        matrix[0][0] = int(s[0] == t[0]) 
        for i in range(1, len(s)):
            currCh = s[i]
            for j in range(len(t)):
                if(s[i] == t[j]):
                    if(j == 0):
                        matrix[i][j] = matrix[i-1][j] + 1
                    else:
                        matrix[i][j] = matrix[i-1][max(0,j-1)] + (matrix[i-1][j])
                else:
                    matrix[i][j] = matrix[i-1][j]
    

        return matrix[len(s)-1][len(t)-1]