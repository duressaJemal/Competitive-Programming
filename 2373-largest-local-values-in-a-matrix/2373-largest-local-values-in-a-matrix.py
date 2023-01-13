# Time: O(N), where N is total number of elements in the grid
# Space: O(N)

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        
        new_grid = [[0] * (n - 2) for _ in range(n - 2)]
        
        row_len = n - 2
        col_len = n - 2
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        
        for row in range(row_len):
            for col in range(col_len):
                
                row_start = row + 1
                col_start = col + 1
                
                max_value = grid[row_start][col_start]
                
                for nr, nc in directions:
                    max_value = max(max_value, grid[row_start + nr][col_start + nc])
                
                new_grid[row][col] = max_value
        
        return new_grid
        
                    
                    
                