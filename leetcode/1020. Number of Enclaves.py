# link: https://leetcode.com/problems/number-of-enclaves/submissions/

# DFS

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        def dfs(r, c):
            
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != 1:
                return
            
            grid[r][c] = 0
            
            for dirc in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                nr = r + dirc[0]
                nc = c + dirc[1]
                dfs(nr, nc)
                
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row in [0, m - 1] or col in [0, n - 1]):
                    dfs(row, col)
        
        count = 0
        for row in range(m):
            for col in range(n):
                count += 1 if grid[row][col] == 1 else 0
                    
        return count



# BFS

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        queue = deque([])
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row in [0, m - 1] or col in [0, n - 1]):
                    queue.append((row, col))
                    grid[row][col] = 0
                    
        while queue:
            
            r, c = queue.popleft()
            
            for dirc in ([1, 0], [0, 1], [-1, 0], [0, -1]):
                nr = r + dirc[0]
                nc = c + dirc[1]
                
                if nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] != 1:
                    continue
                
                grid[nr][nc] = 0
                
                queue.append((nr, nc))
        
        count = 0
        
        for row in range(m):
            for col in range(n):
                count += 1 if grid[row][col] == 1 else 0
                
        
        return count
  
