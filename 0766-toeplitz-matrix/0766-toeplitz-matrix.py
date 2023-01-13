class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        digonal_values = defaultdict(set)
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for row in range(row_len):
            for col in range(col_len):
                digonal_values[row - col].add(matrix[row][col])
        
        for value in digonal_values.values():
            if len(value) > 1:
                return False
        return True
                