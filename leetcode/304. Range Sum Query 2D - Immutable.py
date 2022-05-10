class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        for row in matrix:
            row.insert(0, 0)
            for i in range(1, len(row)):
                row[i] += row[i - 1]
        self.matrix = matrix
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        output = 0
        for i in range(row1, row2 + 1):
            temp = self.matrix[i][col2 + 1] - self.matrix[i][col1]
            output += temp
            
        return output
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
