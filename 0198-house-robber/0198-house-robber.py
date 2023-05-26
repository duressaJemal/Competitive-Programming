class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0] * n
        
        dp[0] = nums[0]
        
        for index in range(1, n):
            dp[index] = max(dp[index - 1], nums[index] + (dp[index - 2] if index > 1 else 0))
            
        return dp[n - 1]
        