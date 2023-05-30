# Time: O(N)
# Space: O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dp(arr):
            
            n = len(arr)
            dp = [0] * n
            
            dp[0] = arr[0]
            
            for i in range(1, n):
                dp[i] = max(dp[i - 1] , dp[i - 2] + arr[i])
            
            return dp[n - 1]
        
        if len(nums) == 1:
            return nums[0]
        
        return max(dp(nums[1:]), dp(nums[:-1]))