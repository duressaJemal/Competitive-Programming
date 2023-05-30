# Bottom-up

# Time: O(N)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        bought, sold = -prices[0], 0
        for i in range(1, len(prices)):
            bought = max(bought, sold - prices[i])
            sold = max(sold, bought + prices[i] - fee)
        
        return max(bought, sold)

# Bottom-up (v2)

# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        
        return max(dp[n - 1][1], dp[n - 1][0])
     

# Top-down

# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        memo = {}
        def helper(i, stock):
            if i == 0:
                if stock: return -prices[0]
                else: return 0
            
            if (i, stock) in memo: return memo[(i, stock)]
            
            memo[(i, 0)] = max(helper(i - 1, 0), helper(i - 1, 1) + prices[i] - fee)
            memo[(i, 1)] = max(helper(i - 1, 1), helper(i - 1, 0) - prices[i])
            
            return memo[(i, stock)]
    
        return max(helper(len(prices) - 1, 1), helper(len(prices) - 1, 0))
    
        