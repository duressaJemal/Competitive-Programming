# Link: https://leetcode.com/problems/max-area-of-island/

# DFS

# time: O(n*m)
# space: O(n*m)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        visited, maximum = set(), 0
        
        def dfs(grid, r, c):
            
            if r < 0 or c < 0 or r >= m or c >= n: return 0
            if grid[r][c] == 0: return 0
            if (r, c) in visited: return 0

            visited.add((r, c))
            
            size = 1
            size += dfs(grid, r - 1, c)
            size += dfs(grid, r + 1, c)
            size += dfs(grid, r, c - 1)
            size += dfs(grid, r, c + 1)
            
            return size
        
        for row in range(m):
            for col in range(n):
                size = dfs(grid, row, col)
                maximum = max(maximum, size)
        
        return maximum

    
# BFS

# time:
# space:

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        nr = [0, 0, -1, 1]
        nc = [-1, 1, 0, 0]
        
        visited, max_area = set(), 0
    
        def bfs(grid, r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            size = 0
            
            while queue:
                r, c = queue.popleft()
                size += 1
                               
                for i in range(4):
                    
                    nw_row = r + nr[i]
                    nw_col = c + nc[i]
                    
                    if nw_row < 0 or nw_row >= m or nw_col < 0 or nw_col >= n:
                        continue
                    if grid[nw_row][nw_col] == 0:
                        continue
                    if (nw_row, nw_col) in visited:
                        continue
                        
                    visited.add((nw_row, nw_col))
                    queue.append((nw_row, nw_col))
            
            return size
            
            
        for row in range(m):
            for col in range(n):
                
                if grid[row][col] == 1 and (row, col) not in visited:
                    size = bfs(grid, row, col)
                    max_area = max(max_area, size)
        
        return max_area
