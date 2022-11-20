# Link: https://leetcode.com/problems/distinct-subsequences/
#Q: 115. Distinct Subsequences

# Top-down

# Time: O(M*N) where M = len(s), N = len(t)
# Space: O(M*N)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def helper(i, j):
            if j == len(t): return 1
            if i == len(s): return 0
            
            if (i, j) in memo: return memo[(i, j)]
            if s[i] == t[j]:
                memo[(i, j)] = helper(i + 1, j) + helper(i + 1, j + 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = helper(i + 1, j)
                return memo[(i, j)]
        
        return helper(0, 0)
    
# Bottom-up

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        
        for r in range(len(s) + 1):
            dp[r][0] = 1
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[len(s)][len(t)]
        

    
