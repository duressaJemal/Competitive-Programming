# Link: https://leetcode.com/problems/minimum-cost-for-tickets/

# Bottom-up

# Time: O(N)
# Space: O(k), where k = 365

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        valid_days = set(days)
        dp = [float("inf") for _ in range(days[-1] + 1)]
        dp[0] = 0
        
        for i in range(1, n + 1):
            if i not in valid_days:
                dp[i] = dp[i - 1]
                continue
            dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
        
        return dp[n]


# Top-down

# Time: O(N)
# Space: O(k), where k = 365

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    
        valid_days = set(days)
        
        @lru_cache(None)
        def dp(i):
            if i == 0: return 0
            elif i in valid_days:
                return min(dp(max(0, i - 1)) + costs[0], dp(max(0, i - 7)) + costs[1], dp(max(0, i - 30)) + costs[2])
            else:
                return dp(max(0, i - 1))
        
        return dp(days[-1])
        
        
        
        
        
            
