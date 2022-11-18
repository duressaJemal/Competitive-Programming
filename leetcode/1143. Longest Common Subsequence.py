# Link: https://leetcode.com/problems/longest-common-subsequence/
#Q: 1143. Longest Common Subsequence

# Bottom-up

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        l1, l2 = len(text1), len(text2)
        dp = [[0] * (l2 + 1)  for _ in range((l1 + 1))]
        
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        return dp[l1][l2]
    
                
# Top-down

# Time: O(M*N) where M = len(text1), N = len(text2)
# space: O(M*N)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}
        def helper(i, j):
            if i < 0 or j < 0: return 0
            if i == 0 and j == 0:
                if text1[i] == text2[j]: return 1
                else: return 0
            
            if (i, j) in memo: return memo[(i, j)]
            if text1[i] == text2[j]:
                memo[(i, j)] = helper(i - 1, j - 1) + 1
            else:
                memo[(i, j)] = max(helper(i - 1, j), helper(i, j - 1))
                
            return memo[(i, j)]
        return helper(len(text1) - 1, len(text2) - 1)
                

                
                
