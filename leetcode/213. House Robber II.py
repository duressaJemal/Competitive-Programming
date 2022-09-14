# Link: https://leetcode.com/problems/house-robber-ii/

# Bottom-up(space-optimized)

# Time: O(N)
# Space: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def linear_rob(nums, rob_first_house):
            left, right = 0, 0
            for i in range(n - 1) if rob_first_house else range(1, n):
                temp = right
                left = max(left + nums[i], right)
                right, left = left, temp
            return right
    
        if len(nums) == 1: return nums[0]
        return max(linear_rob(nums, True), linear_rob(nums, False))
            
        
# Bottom-up

# Time: O(N)
# Space: O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def linear_rob(nums):
            
            n = len(nums)
            dp = [0] * n
            dp[0] = nums[0]

            for i in range(1, n):
                dp[i] = max(dp[i - 1], nums[i] + (dp[i - 2] if i > 1 else 0))
            return dp[n - 1]
        
        
        return nums[0] if len(nums) == 1 else max(linear_rob(nums[1:]), linear_rob(nums[:-1]))
            
# Top-down:

# Time: O(N)
# Space: O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def linear_rob(nums):
            n = len(nums)
            memo = {}
            
            def dp(i):
                if i < 0: return 0
                if i == 0: return nums[0]
                if i in memo: return memo[i]
                memo[i] = max(dp(i - 1), nums[i] + dp(i - 2))
                return memo[i]
                
            return dp(n - 1)
        
        return nums[0] if len(nums) == 1 else max(linear_rob(nums[1:]), linear_rob(nums[:-1]))
    

        
