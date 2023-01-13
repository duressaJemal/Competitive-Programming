# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        digonal_values = defaultdict(int)
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for row in range(row_len):
            for col in range(col_len):
                digonal_values[row - col].add(matrix[row][col])
        
        for value in digonal_values.values():
            if len(value) > 1:
                return False
        return True
            

# optimized

# Time: O(M*N)
# Space: O(1)

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for row in range(row_len - 1):
            for col in range(col_len - 1):
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False
        
        return True
        
        
        
        
        
        
        
        
        
        
