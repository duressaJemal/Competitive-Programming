# link https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        memo = {}
        
        def helper(r, c):
            
            if (r, c) in memo: return memo[(r, c)]
            if r == m - 1 and c == n - 1: return grid[r][c]
            if r >= m or c >= n: return float("inf")
            
            memo[(r, c)] =  grid[r][c] + min(helper(r + 1, c), helper(r, c + 1))
            return memo[(r,c)]
        
        return helper(0, 0)
        
        
