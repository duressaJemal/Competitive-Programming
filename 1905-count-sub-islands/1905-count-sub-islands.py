class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def dfs(row, col):
            # out of bound for both grids       
            if row < 0 or row >= row_len or col < 0 or col >= col_len:
                return True
            if grid2[row][col] == 0: 
                return True
            
            cur = True
            if grid2[row][col] == 1 and grid1[row][col] == 0: 
                cur = False
            
            # mark
            visited.add((row, col))
            
            dirc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for x, y in dirc:
                nr = x + row
                nc = y + col
                
                if (nr, nc) not in visited:
                    cur = dfs(nr, nc) and cur # avoid short circuit
            
            return cur
        
        row_len = len(grid1)
        col_len = len(grid1[0])

        visited = set()
        count = 0
        
        for row in range(row_len):
            for col in range(col_len):
                if (row, col) not in visited and grid2[row][col]:
                    if dfs(row, col):
                        count += 1
        
        return count
                    
            
        
                
                
            
                
            