# Link: https://leetcode.com/problems/climbing-stairs/
#Q: 70. Climbing Stairs

# Bottom-up

# Time: O(N)
# Space: O(N)

class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        
        for i in range(2, n + 1):
            for j in [1, 2]:
                if j <= i:
                    dp[i] += dp[i - j]
                    
        return dp[n]

# Top-down

# Time: O(N)
# Space: O(N)

class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        
        def helper(i):
            if i == 0 or i == 1: return 1
            if dp[i] != 0: return dp[i]
            dp[i] = helper(i - 1) + helper(i - 2)
            return dp[i]
        
        return helper(n)
        
        
        
        
        
