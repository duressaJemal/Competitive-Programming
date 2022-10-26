# Link: https://leetcode.com/problems/last-stone-weight-ii/
#Q: 1049. Last Stone Weight II

# Top-down

# Time: O(N*2)
# Space: O(N*2)

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total = sum(stones)
        lower_bound = total // 2
        n = len(stones)
        dp = [[False for _ in range(lower_bound + 1)] for _ in range(n + 1)]
        
        # classical knapsack
        
        for i in range(n + 1):
            for j in range(lower_bound + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                
                elif j >= stones[i - 1]:
                    dp[i][j] = max(stones[i - 1] + dp[i - 1][j - stones[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return total - (2 * dp[i][j]) # main intuition


    
