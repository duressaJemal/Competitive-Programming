# Link: https://leetcode.com/problems/longest-palindromic-subsequence/
#Q: 516. Longest Palindromic Subsequence

# Top-down

# Time: O(N*2)
# Space: O(N*2)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        memo = {}
        def helper(i, j):
            if i == j: return 1
            if i > j: return 0
            
            if (i, j) in memo: return memo[(i, j)]
            
            if s[i] == s[j]:
                memo[(i, j)] = helper(i + 1, j - 1) + 2
            else:
                memo[(i, j)] = max(helper(i + 1, j), helper(i, j - 1))
            return memo[(i, j)]
        return helper(0, len(s) - 1)
    

# Bottom-up

# Time: O(N*2)
# Space: O(N*2)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = [[0] * (len(s)) for _ in range(len(s))]
        for l in range(len(s)):
            for i in range(len(s) - l):
                j = i + l
                if i == j:
                    dp[i][j] = 1
                elif j == i + 1:
                    dp[i][j] = 2 if s[i] == s[j] else 1
                else:
                    dp[i][j] = (2 + dp[i + 1][j - 1]) if s[i] == s[j] else max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][len(s) - 1]
    
# ALTERNATIVE

#         dp = [[0] * (len(s)) for _ in range(len(s))]
#         for i in range(len(s)):
#             dp[i][i] = 1
            
#         for r in range(len(s)):
#             for l in range(r - 1, -1, -1):
#                 dp[l][r] = (2 + dp[l + 1][r - 1]) if s[l] == s[r] else max(dp[l + 1][r], dp[l][r - 1])
        
#         return dp[0][len(s) - 1]
        
        


            
        
        
            
            
            
