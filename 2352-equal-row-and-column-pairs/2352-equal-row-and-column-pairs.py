class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        row_elements = {}
        col_elements = {}
        
        row_len = len(grid[0])
        col_len = row_len
        
        for index, row in enumerate(grid):
            row_elements[index] = tuple(row)
            
        for col in range(col_len):
            temporary = []
            for row in range(row_len):
                temporary.append(grid[row][col])
            
            col_elements[col] = tuple(temporary)
        
        
        equal_pairs = 0
        for row in range(row_len):
            for col in range(col_len):
                if row_elements[row] == col_elements[col]:
                    equal_pairs += 1
        
        return equal_pairs
                
        
        
        
        
        