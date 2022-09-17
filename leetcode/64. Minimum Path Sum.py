# Link: https://leetcode.com/problems/minimum-path-sum/

# Bottom-up

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[m - 1][n - 1]

# Top-down

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        memo = {}
        
        def helper(r, c):
            if r == 0 and c == 0: return grid[0][0]
            if r < 0 or c < 0: return float("inf")
            
            if (r, c) in memo: return memo[(r, c)]
            
            memo[(r, c)] = min(helper(r - 1, c), helper(r, c - 1)) + grid[r][c]
            return memo[(r, c)]
        
        return helper(m - 1, n - 1)
        
        
        
