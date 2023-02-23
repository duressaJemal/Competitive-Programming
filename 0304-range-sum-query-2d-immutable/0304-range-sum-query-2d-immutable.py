class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        prefix = [[0 for _ in range(col_len + 1)] for _ in range(row_len + 1)]
        
        # build prefix
        for row in range(1, row_len + 1):
            for col in range(1, col_len + 1):
                
                prefix[row][col] = prefix[row - 1][col] + prefix[row][col - 1] + matrix[row - 1][col - 1] - prefix[row - 1][col - 1]
                
        self.matrix = prefix
        print(self.matrix)
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        val = self.matrix[row2 + 1][col2 + 1] - self.matrix[row1][col2 + 1] - self.matrix[row2 + 1][col1] + self.matrix[row1][col1]
        
        return val


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)