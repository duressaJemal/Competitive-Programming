# Time: O(M*N * (M + N))
# Space: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for row in range(row_len):
            for col in range(col_len):
                
                if matrix[row][col] == 0:
                    # change it's row and col neighbours into temporary "#"
                    for r in range(row_len):
                        if matrix[r][col] != 0:
                            matrix[r][col] = "#"
                    
                    for c in range(col_len):
                        if matrix[row][c] != 0:
                            matrix[row][c] = "#"
        
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == "#":
                    matrix[row][col] = 0
        
        
        
                    