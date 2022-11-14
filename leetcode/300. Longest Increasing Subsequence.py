# Link: https://leetcode.com/problems/longest-increasing-subsequence/
#Q: 300. Longest Increasing Subsequence

# Bottom-up

# Time: O(N*2)
# Space: O(N)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
    
        return max(dp)

# Top-down

# Time: O(N*2)
# Space: O(N)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)
        dp[0] = 1
        
        def helper(i):
            if i == 0: return 1
            if dp[i] != 0: return dp[i]
            
            dp[i] = 1
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], helper(j) + 1)
            return dp[i]
        
        for i in range(len(nums)):
            helper(i)
            
        return max(dp)
            
            
            
