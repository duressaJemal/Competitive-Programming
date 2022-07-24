# link: https://leetcode.com/problems/number-of-islands/

# time: O(n*m)
# space: O(n*m)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m , n = len(grid), len(grid[0])
        visited, count = set(), 0
        
        def dfs(grid, r, c):
            
            if r < 0 or c < 0 or r >= m or c >= n: return False
            if grid[r][c] == "0": return False
            if (r, c) in visited: return False
            
            visited.add((r, c))
            
            dfs(grid, r - 1, c)
            dfs(grid, r + 1, c)
            dfs(grid, r, c - 1)
            dfs(grid, r, c + 1)
            
            return True

        for row in range(m):
            for col in range(n):
                
                if dfs(grid, row, col):
                    count += 1
                
        return count
        
