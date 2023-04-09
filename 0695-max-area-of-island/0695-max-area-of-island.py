class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        def is_valid(row, col):
            if row < 0 or row >= row_len or col < 0 or col >= col_len or grid[row][col] == 0:
                return False
            else:
                return True
            
        def dfs(row, col):
            # base case
            if not is_valid(row, col):
                return 0
            
            grid[row][col] = 0
            count = 1
            
            dirc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            for x, y in dirc:
                nr = row + x
                nc = col + y
                count += dfs(nr, nc)
            
            return count
        
        res = 0
        for row in range(row_len):
            for col in range(col_len):
                res = max(res, dfs(row, col))
        return res
                    
        
        
        
        