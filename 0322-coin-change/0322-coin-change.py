class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [float("inf")] * (amount + 1)
        
        # base case
        dp[0] = 0
        
        for money in range(1, amount + 1):
            for coin in coins:
                if coin <= money and dp[money - coin] != float("inf"):
                    dp[money] = min(dp[money], dp[money - coin] + 1)
        
        return dp[amount] if dp[amount] != float("inf") else -1