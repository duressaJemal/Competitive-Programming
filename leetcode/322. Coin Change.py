# Link: https://leetcode.com/problems/coin-change/
#Q: 322. Coin Change

# Bottom-up

# Time: O(N*k)
# Space: O(N*k)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    
        return -1 if dp[amount] == float("inf") else dp[amount]
                       
# Top-down

# Time: O(N*K)
# Space: O(N*K)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        
        def dp(i):
            if not i: return 0
            if i in memo: return memo[i]
            
            memo[i] = float("inf")
            for coin in coins:
                if coin <= i:
                    memo[i] = min(memo[i], dp(i - coin) + 1)
            
            return memo[i]
        
        return -1 if dp(amount) == float("inf") else dp(amount)
        
        
