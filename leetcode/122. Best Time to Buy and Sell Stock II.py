# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#Q: 122. Best Time to Buy and Sell Stock II

# Bottom-up

# Time: O(N)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        bought, sold = -prices[0], 0
        for i in range(1, len(prices)):
            bought = max(bought, sold - prices[i])
            sold = max(sold, bought + prices[i])
            
        return sold
