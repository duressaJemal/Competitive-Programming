# Link: https://leetcode.com/problems/unique-paths/
#Q: 62. Unique Paths.py

# Bottom-up

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i == 0: 
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:    
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]
    

# Top-down

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        def helper(i, j):
            if i == 0 or j == 0: return 1
            if dp[i][j] != 0: return dp[i][j]
            
            dp[i][j] = helper(i, j - 1) + helper(i - 1, j)
            return dp[i][j]
        
        return helper(m - 1, n - 1)
        

        
        
    
