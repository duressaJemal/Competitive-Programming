# Link: https://leetcode.com/problems/swim-in-rising-water/

# Binary search + BFS

# Time: O(N^2 * log(N))
# Space: O(N^2)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        largest = 0
        
        for row in range(m):
            for col in range(n):
                largest = max(largest, grid[row][col])
        
        # BFS
        
        def is_good(x):
            queue = deque([(0, 0)])
            visited = set()
            
            while queue:
                r, c = queue.popleft()
                if (r, c) == (n - 1, n - 1):
                    return True
                for row, col in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr = r + row
                    nc = c + col
                    
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr, nc) in visited: continue
                    
                    if grid[nr][nc] <= x:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        
            return False
                
        
        # Binary search
        
        left = -1
        right = largest
        
        while right > left + 1:
            
            mid = (left + right) // 2
            if is_good(mid):
                right = mid
            else:
                left = mid
        return max(right, grid[0][0])
