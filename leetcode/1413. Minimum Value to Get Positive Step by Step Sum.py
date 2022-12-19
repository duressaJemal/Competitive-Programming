# Link: https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
#Q: 1413. Minimum Value to Get Positive Step by Step Sum

# Time: O(N)
# Space: O(1)

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        mn = nums[0]
        
        for i in range(1, n):
            nums[i] += nums[i - 1]
            mn = min(mn, nums[i])
        
        if mn >= 0: return 1
        if mn < 0: return 0 - (mn - 1)
        
