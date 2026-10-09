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
    
        transposed_matrix = list(zip(*matrix))

        # Calculate padding based on the longest string/number element
        col_width = max(len(str(item)) for row in matrix for item in row) + 2

        # 2. Print the top header (string 's' now running horizontally)
        print(" " * col_width + "".join(f"{char:<{col_width}}" for char in s))

        # 3. Print the rows (string 't' now running vertically down the side)
        for i, row in enumerate(transposed_matrix):
            row_str = "".join(f"{item:<{col_width}}" for item in row)
            print(f"{t[i]:<{col_width}}{row_str}")

        return matrix[len(s)-1][len(t)-1]