# Link: https://leetcode.com/problems/min-cost-climbing-stairs/

# Bottom-up

# Time: O(N)
# Space: O(N)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
            
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        
        return min(dp[n - 1], dp[n - 2])
    
# Bottom-up(space-optimized)

# Time: O(N)
# Space: O(1)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        left = cost[0]
        right = cost[1]
        
        for i in range(2, n):
            temp = right
            left = min(left, right) + cost[i]
            right, left = left, temp
        
        return min(left, right)
            
