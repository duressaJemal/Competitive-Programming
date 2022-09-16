# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Bottom-up

# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        price_gap = 0
        
        dp = [0] * n
        dp[0] = prices[0]
        
        for i in range(1, n):
            dp[i] = min(dp[i - 1], prices[i])
            price_gap = max(price_gap, prices[i] - dp[i])
        
        return price_gap

# Ad-hoc

# Time: O(N)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        smallest = prices[0]
        price_gap = 0
        
        for i in range(1, n):
            smallest = min(smallest, prices[i])
            price_gap = max(price_gap, prices[i] - smallest)
        
        return price_gap
        

            
