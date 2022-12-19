# Link: https://leetcode.com/problems/number-of-ways-to-split-array/
#Q: 2270. Number of Ways to Split Array

# Time: O(N)
# Space: O(1)

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        
        count = 0
        for i in range(n):
            if nums[i] >= (nums[-1] - nums[i]) and i < n - 1:
                count += 1
        
        return count
