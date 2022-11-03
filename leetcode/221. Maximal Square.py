# Link: https://leetcode.com/problems/maximal-square/
#Q: 221. Maximal Square

# Bottom-up

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_square = 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_square = max(max_square, dp[i][j])
                    
        return max_square * max_square
    

# Top-down

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        memo = {}
        max_square = 0
        
        def helper(i, j):
            if i < 0 or i == m or j < 0 or j == n: return 0
            if matrix[i][j] == "0": return 0
            
            if (i, j) in memo: return memo[(i, j)]
            memo[(i, j)] =  min(helper(i - 1, j), helper(i, j - 1), helper(i - 1, j - 1)) + 1
            return memo[(i, j)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    max_square = max(max_square, helper(i, j))
                    
        return max_square * max_square
    
        
