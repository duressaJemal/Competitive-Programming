#link https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]        
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            
            if current_sum + nums[i] < nums[i]:
                current_sum = nums[i]
            else:
                current_sum += nums[i]
            
            max_sum = max(current_sum, max_sum)
        
        return max_sum
