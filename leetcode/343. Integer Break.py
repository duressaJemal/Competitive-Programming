# Link: https://leetcode.com/problems/integer-break/
#Q: 343. Integer Break

# Top-down

# Time: O(N)
# Space: O(N)

class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [0] * (n)
        def helper(n):
            if n <= 1: return 1
            if dp[n] != 0: return dp[n]
            for i in range(1, n + 1):
                dp[n] = max(dp[n], i * helper(n - i))
            return dp[n]
        
        mx = 0
        for i in range(1, n):
            mx = max(mx, i * helper(n - i))
        
        return mx
    
# Bottom-up

# Time: O(N)
# Space: O(N)

class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [1] * (n + 1)
        
        for k in range(2, n + 1):
            i = 1
            j = k - 1
            
            mx = 0
            while i <= j:
                mx = max(mx, max(i, dp[i]) * max(j, dp[j]))
                i += 1
                j -= 1
            dp[k] = mx
            
        return dp[k]
            
            
            
        
        
        
