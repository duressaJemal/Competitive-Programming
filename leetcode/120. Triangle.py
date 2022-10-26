# Link: https://leetcode.com/problems/triangle/
#Q: 120. Triangle

# Bottom-up(space optimized)

# Time: O(N*2)
# Space: O(N)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = [0] * (len(triangle[-1]) + 1)
        
        for r in range(len(triangle) - 1, -1, -1):
            for c in range(len(triangle[r])):
                dp[c] = min(dp[c], dp[c + 1]) + triangle[r][c]
        return dp[0]
      
        
# Bottom-up

# Time: O(N*2)
# Space: O(N*2)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = [[0 for _ in range(201)] for _ in range(201)]

        for r in range(len(triangle) - 1 , -1, -1):
            for c in range(len(triangle[r])):
                dp[r][c] = min(dp[r + 1][c], dp[r + 1][c + 1]) + triangle[r][c]
        
        return dp[0][0]
            

