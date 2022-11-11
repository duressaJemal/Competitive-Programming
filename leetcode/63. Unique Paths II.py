# Link: https://leetcode.com/problems/unique-paths-ii/
#Q: 63. Unique Paths II

# Bottom-up

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0] * (n) for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: 
                    continue
                
                elif i == 0:
                    value = 0 if obstacleGrid[i][j - 1] == 1 else dp[i][j - 1]
                    dp[i][j] = value
                elif j == 0:
                    value = 0 if obstacleGrid[i - 1][j] == 1 else dp[i - 1][j]
                    dp[i][j] = value
                else:
                    left = 0 if obstacleGrid[i][j - 1] == 1 else dp[i][j - 1]
                    right = 0 if obstacleGrid[i - 1][j] == 1 else dp[i - 1][j]
                    dp[i][j] = left + right
        
        return  0 if obstacleGrid[m - 1][n - 1] else dp[m - 1][n - 1]
                
        
# Top-down

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[-1] * (n) for _ in range(m)]
        def helper(i, j):
            if i < 0 or j < 0 or i >= m or j >= n: return 0
            if obstacleGrid[i][j] == 1: return 0
            if i == 0 and j == 0: return 1
            
            if dp[i][j] != -1: return dp[i][j]
            
            left = helper(i, j - 1)
            top  = helper(i - 1, j)
            
            dp[i][j] = left + top
            return dp[i][j]
        
        return helper(m - 1, n - 1)
    


        
        
        
