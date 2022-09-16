# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# DP(Bottom-up)

# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        have_stock = [0] * n
        dont_have_stock = [0] * n
        
        have_stock[0] = -prices[0]
        
        maximum = 0
        
        for i in range(1, n):
            have_stock[i] = max((dont_have_stock[i - 2] - prices[i]) if i > 1 else  0 - prices[i], have_stock[i - 1])
            dont_have_stock[i] = max(dont_have_stock[i - 1], have_stock[i - 1] + prices[i])
            
            
        # print("have stock ", have_stock)
        # print("dont have stock", dont_have_stock)
        
        return max(have_stock[n - 1], dont_have_stock[n - 1])
            
