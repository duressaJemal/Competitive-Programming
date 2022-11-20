# Link: https://leetcode.com/problems/edit-distance/
#Q: 72. Edit Distance

# Top-down

# Time: O(M*N) where M = len(word1) , N = len(word2)
# Space: O(M*N)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def helper(i, j):
            if i < 0 and j < 0: return 0
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            
            if (i, j) in memo: return memo[(i, j)]
            if word1[i] == word2[j]:
                memo[(i, j)] = helper(i - 1, j - 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = min(helper(i, j - 1), helper(i - 1, j), helper(i - 1, j - 1)) + 1
                return memo[(i, j)]
                
        
        return helper(len(word1) - 1, len(word2) - 1)

# Bottom-up

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        

        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                
                else:
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    
        return dp[len(word1)][len(word2)]
             
             
             
             
             
