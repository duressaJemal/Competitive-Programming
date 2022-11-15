# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#Q: 121. Best Time to Buy and Sell Stock

# Bottom-up(space optimized)

# Time: O(N)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        smallest = prices[0]
        output = 0
        
        for i in range(1, len(prices)):
            smallest = min(smallest, prices[i])
            output = max(output, prices[i] - smallest)
        
        return output


# Bottom-up

# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [0] * (len(prices))
        dp[0] = prices[0]
        output = 0
        
        for i in range(1, len(prices)):
            dp[i] = min(dp[i - 1], prices[i])
            output = max(output, prices[i] - dp[i])
        
        return output



# Prefix

# Time: O(N)
# Space: O(N)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        mx = 10001
        
        prefix, sufix = [mx] * (n + 1), [-1] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = min(prefix[i - 1], prices[i - 1])
        for i in range(n - 1, -1, -1):
            sufix[i] = max(sufix[i + 1], prices[i])
        output = 0
        for i in range(1, n + 1):
            output = max(output, sufix[i] - prefix[i])
        return output
                
