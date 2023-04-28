# Time: O(V + E)
# Space: O(V)

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        def is_valid(row, col):
            
            if row < 0 or col < 0 or row >= row_len or col >= col_len:
                return False
            else:
                return True
            
        queue = deque([(0,0)] if not grid[0][0] else [])
        visited = {(0, 0)}
        
        level = 0
        dirc = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        while queue:
            
            n = len(queue)
            for _ in range(n):
                
                row, col = queue.popleft()
                if grid[row][col] == 0 and (row == row_len - 1 and col == col_len - 1):
                    return level + 1
                
                for x, y in dirc:
                    nr = row + x
                    nc = col + y
                    
                    if is_valid(nr, nc) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            
            level += 1
        
        return -1 
        
                    
                    
                        
                        
                        
                        
                        
                
                
            
            