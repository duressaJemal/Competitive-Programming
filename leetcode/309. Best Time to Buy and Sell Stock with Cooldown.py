# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
#Q: 309. Best Time to Buy and Sell Stock with Cooldown

# Bottom-up

# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = [[0, 0] for _ in range(n)] 
        dp[0][1] = -prices[0]
        
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], (dp[i - 2][0] if i > 1 else 0) - prices[i])
        
        return max(dp[n - 1][0], dp[n - 1][1])

# Top-down

# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def helper(i, stock):
            
            if i < 0: return 0
            if i == 0:
                if stock: return - prices[0]
                else: return 0
            if (i, stock) in memo: return memo[(i, stock)]
            
            memo[(i, 1)] = max(helper(i - 1, 1), helper(i - 2, 0) - prices[i])
            memo[(i, 0)] = max(helper(i - 1, 0), helper(i - 1, 1) + prices[i])
            
            return memo[(i, stock)]
        
        return max(helper(len(prices) - 1, 1), helper(len(prices) - 1, 0))
        

    
# Bottom-up(v2)

# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        have_stock = [0] * n
        dont_have_stock = [0] * n
        have_stock[0] = -prices[0]
        
        for i in range(1, n):
            have_stock[i] = max(have_stock[i - 1], (dont_have_stock[i - 2] if i > 1 else 0) - prices[i])
            dont_have_stock[i] = max(dont_have_stock[i - 1], have_stock[i - 1] + prices[i])
        
        return max(have_stock[n - 1], dont_have_stock[n - 1])
