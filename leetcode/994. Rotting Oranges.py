# Link: https://leetcode.com/problems/rotting-oranges/

# BFS

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        queue = deque([])
        
        # explore rotten oranges
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
        
        count = 0

        while queue:
            
            count += 1
            length = len(queue)
    
            for _ in range(length):
                
                r, c = queue.popleft()
                
                for dirc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    
                    nr = r + dirc[0]
                    nc = c + dirc[1]
            
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] != 1:
                        continue
                    
                    queue.append((nr, nc))
                    grid[nr][nc] = 2
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    return -1
        
        return count - 1 if count else 0
            
            
