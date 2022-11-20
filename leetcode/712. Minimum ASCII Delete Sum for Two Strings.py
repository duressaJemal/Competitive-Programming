# Link: https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/
#Q: 712. Minimum ASCII Delete Sum for Two Strings

# Top-down

# Time: O(L1*L2)
# Space: O(L1*L2)

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        # first column base case
        for c in range(1, len(s2) + 1):
            dp[0][c] = dp[0][c - 1] + ord(s2[c - 1])
            
        # first row base case
        for r in range(1, len(s1) + 1):
            dp[r][0] = dp[r - 1][0] + ord(s1[r - 1])
            
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
                
        return dp[len(s1)][len(s2)]
                    
                    
# Bottom-up

# Time: O(L1*L2)
# Space: O(L1*L2)

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        memo = {}
        def helper(i, j):
            if i < 0 and j < 0: return 0
            if (i, j) in memo: return memo[(i, j)]
            
            if i < 0:
                val = 0
                for t in range(j + 1):
                    val += ord(s2[t])
                return val
            if j < 0:
                val = 0
                for t in range(i + 1):
                    val += ord(s1[t])
                return val
            
            if s1[i] == s2[j]:
                memo[(i, j)] = helper(i - 1, j - 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = min(helper(i - 1, j) + ord(s1[i]), helper(i, j - 1) + ord(s2[j]))
                return memo[(i, j)]
        
        return helper(len(s1) - 1, len(s2) - 1)
