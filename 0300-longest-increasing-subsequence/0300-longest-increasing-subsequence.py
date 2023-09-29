# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         dp = [1] * n
        
#         for i in range(n):
#             for j in range(0, i):
                
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)
            
#         return max(dp)
      

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @cache
        def dp(index):
            
            if index == 0:
                return 1

            mx = 1
            for i in range(index - 1, -1, -1):
                if nums[i] < nums[index]:
                    mx = max(mx, dp(i) + 1)
                
            return mx
    
        n = len(nums)
        
        output = 0
        for i in range(n):
            output = max(output, dp(i))
        
        return output
        
        
                
            