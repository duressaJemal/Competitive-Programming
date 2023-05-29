# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                
                if row == 0 or col == 0:
                    dp[row][col] = 1
                    continue
                
                left = dp[row][col - 1] if col >= 0 else 0
                top = dp[row - 1][col] if row >= 0 else 0
                dp[row][col] = left + top
            
         
        print(dp)
        return dp[m - 1][n - 1]
        
        