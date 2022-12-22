# Link: https://leetcode.com/problems/missing-number/
#Q: 268. Missing Number

# Time: O(N)
# Space: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)
