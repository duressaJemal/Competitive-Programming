class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        
        return dp[m - 1][n - 1]
                
                