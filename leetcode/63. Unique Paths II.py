# link https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        memo = {}
        
        def helper(r, c):
            
            if (r, c) in memo: return memo[(r, c)]
            if r == m or c == n or obstacleGrid[r][c] == 1: return 0
            if r == m - 1 and c == n - 1: return 1
            
            memo[(r,c)] =  helper(r + 1, c) + helper(r, c + 1)
            
            return memo[(r, c)]
        
        return helper(0, 0)
