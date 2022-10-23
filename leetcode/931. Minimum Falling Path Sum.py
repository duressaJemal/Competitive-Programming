# Link: https://leetcode.com/problems/minimum-falling-path-sum/submissions/
#Q: 931. Minimum Falling Path Sum

# Top-down

# Time: O(N*2)
# Space: O(N*2)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        MAX = float("inf")
        
        dp = [[MAX for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, n):
            for j in range(n):
                dp[i][j] = min(dp[i - 1][j] , dp[i - 1][j - 1] if j > 0 else MAX, dp[i - 1][j + 1] if j + 1 < n else MAX) + matrix[i][j]
                
        mn = MAX
        for i in range(n):
            mn = min(mn, dp[n - 1][i])
        
        return mn


# Bottom-up

# Time: O(N*2)
# Space: O(N*2)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        memo = [[float("inf") for _ in range(n)] for _ in range(n)]
        
        def dp(i, j):
            if i < 0 or j > n - 1 or j < 0: return float("inf")
            if i == 0: return matrix[i][j]
            if memo[i][j] != float("inf"): return memo[i][j]
            
            memo[i][j] = min(dp(i - 1, j), dp(i - 1, j - 1), dp(i - 1, j + 1)) + matrix[i][j]
            return memo[i][j]
    
        mn = float("inf")
        for j in range(n):
            mn = min(mn, dp(n - 1, j))
        
        return mn
