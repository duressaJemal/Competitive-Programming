class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        # row prefix
        for col in range(1, col_len):
            matrix[0][col] += matrix[0][col - 1]
        
        # col prefix
        for row in range(1, row_len):
            matrix[row][0] += matrix[row - 1][0]
        
        
        # build prefix
        for row in range(1, row_len):
            for col in range(1, col_len):
                
                up = matrix[row - 1][col]
                left = matrix[row][col - 1]
                digonal = matrix[row - 1][col - 1] 
                current = matrix[row][col]
                
                matrix[row][col] = up + left + current - digonal 
    
        self.matrix = matrix

                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        up_right = self.matrix[row1 - 1][col2] if row1 else 0
        bottom_left = self.matrix[row2][col1 - 1] if col1 else 0 
        digonal = self.matrix[row1 - 1][col1 - 1] if (col1 and row1) else 0 
        
        return self.matrix[row2][col2] - up_right - bottom_left + digonal


        
        



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)