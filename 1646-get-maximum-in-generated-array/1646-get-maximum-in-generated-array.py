# Time: O(N)
# Space: O(N)

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if not n:
            return 0
        
        mx = 1
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            index = i // 2
            dp[i] = dp[index]
            if i % 2:
                dp[i] += dp[index + 1]
        
            mx = max(mx, dp[i])
        
        return mx
        
        
        