# Link: https://leetcode.com/problems/house-robber/
#Q: 198. House Robber

# Bottom-up (v1)

# Time: O(N)
# Space: O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [[0] * 2 for _ in range(len(nums) + 1)]
        
        for i in range(1, len(nums) + 1):
            dp[i][1] = max(dp[i - 1][0] + nums[i - 1], dp[i - 1][1])
            dp[i][0] = dp[i - 1][1]
        
        return dp[len(nums)][1]

# Bottom-up (v2)

# Time: O(N)
# Space: O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max((dp[i - 2] if i > 1 else 0) + nums[i], dp[i - 1])
        return dp[len(nums) - 1]
        
# Top-down

# Time: O(N)
# space: O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [-1] * (len(nums))
        def helper(i):
            if i < 0: return 0
            if dp[i] != -1: return dp[i]
            
            dp[i] = max(helper(i - 1), helper(i - 2) + nums[i])
            return dp[i]
        
        return helper(len(nums) - 1)
            
