# Link: https://leetcode.com/problems/min-cost-climbing-stairs/

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
            
        
# Bottom-up

# Time: O(N)
# Space: O(N)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1], dp[i - 2]) + (cost[i] if i < n else 0)
        
        return dp[n]
        
# Top-down

# Time: O(N)
# Space: O(N)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        
        def minCost(n):
            
            if n == 0 or n == 1: return cost[n]
            if n in memo: return memo[n]
            
            memo[n] = min(minCost(n - 1), minCost(n - 2)) + (cost[n] if n < len(cost) else 0)
            return memo[n]
        
        return minCost(n)
            
        

        
        
        
        
        
        
        
