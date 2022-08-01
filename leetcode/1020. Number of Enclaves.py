# link: https://leetcode.com/problems/number-of-enclaves/submissions/

# DFS

# time: O(n*m)
# space: O(n*m)


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        count = 0
        
        def dfs(r, c):
            
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != 1:
                return
            
            grid[r][c] = 0
            
            for dirc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = r + dirc[0]
                nc = c + dirc[1]
                
                dfs(nr, nc)
            
            
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row in [0, m - 1] or col in [0, n - 1]):
                    dfs(row, col)
              
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    count += 1
        
        return count
                

# BFS

# time: O(n*m)
# space: O(n*m)

        
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        queue = deque([])
        
        for row in range(m):
            for col in ([0, n - 1]):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    queue.append((row, col))
                
        for row in ([0, m - 1]):
            for col in range(1, n):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    queue.append((row, col))
                
        
        while queue:
            
            row, col = queue.popleft()
            for dirc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr = row + dirc[0]
                nc = col + dirc[1]
                
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                    
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    queue.append((nr, nc))
             
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    count += 1
        
        return count
