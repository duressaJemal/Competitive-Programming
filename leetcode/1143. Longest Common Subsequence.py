# link: https://leetcode.com/problems/longest-common-subsequence/

# Top-down
    
    # time: O(n * m)
    # space: O(n * m)
    
class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)
        memo = {}
        
        def lcf(x, y, m, n, memo):
            if m <= 0 or n <= 0:
                return 0
            if (m , n) in memo:
                return memo[(m, n)]
            if x[m - 1] == y[n - 1]:
                memo[(m, n)] = 1 + lcf(x, y, m - 1, n - 1, memo)
                return memo[(m, n)]
            
            memo[(m, n)] =  max(lcf(x, y, m, n - 1, memo), lcf(x, y, m - 1, n, memo))
            return memo[(m, n)]
        return lcf(text1, text2, m, n, memo)

# Bottom-up ----Not working
# push dp

# # time: O(m * n)
# # space: O(m * n)

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:

#         m = len(text1)
#         n = len(text2)
#         dp = [[0] * (n + 1)] * (m + 1)
        
#         for i in range(m):
#             for j in range(n):
#                 if text1[i] == text2[j]:
#                     dp[i + 1][j + 1] = dp[i][j] + 1
#                 else:
#                     dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
#         return dp[m][n]


# Bottom up
# Pull dp

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:

#         m = len(text1)
#         n = len(text2)
        
#         dp = [[0] * (n + 2)] * (m + 2)
        
#         for i in range(m + 1):
#             for j in range(n + 1):
                
#                 if i == 0 or j == 0:
#                     dp[i][j] == 0
                
#                 else:
#                     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#                     if text1[i - 1] == text2[j - 1]:
#                         dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
                    
        
#         print(dp)
#         return dp[i][j]
    
    

