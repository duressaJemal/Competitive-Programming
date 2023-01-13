class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        row_len = len(mat)
        col_len = len(mat[0])
        
        # check equality of the two grids
        if row_len * col_len != r * c:
            return mat
        
        new_matrix = [[0] * c for _ in range(r)]
        new_matrix_row = 0
        new_matrix_col = 0
        
        for row in range(row_len):
            for col in range(col_len):
                
                if new_matrix_col >= c:
                    new_matrix_row += 1
                    new_matrix_col = 0 
                    
                new_matrix[new_matrix_row][new_matrix_col] = mat[row][col]
                new_matrix_col += 1
        
        return new_matrix

                    
        
        