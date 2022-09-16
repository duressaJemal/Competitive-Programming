# link https://leetcode.com/problems/minimum-path-sum/

# Time: O(M*N)
# Space: O(M*N)

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
        
        


# Bottom-up

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == j == 0: continue
                dp[i][j] = min(dp[i - 1][j] if i > 0 else float("inf"), dp[i][j - 1] if j > 0 else float("inf")) + grid[i][j]
        
        return dp[m - 1][n - 1]
