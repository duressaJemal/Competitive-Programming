# Link: https://leetcode.com/problems/house-robber/

# Bottom-up

# Time: O(N)
# Space: O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0] * n
        
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(dp[i - 1], nums[i] + (dp[i - 2] if i > 1 else 0))
        
        return dp[n - 1]

# Top-down

# Time: O(N)
# Space: O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(i):
            if i < 0: return 0
            if i == 0: return nums[i]
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            return memo[i]
        
        return dp(len(nums) - 1)
            
