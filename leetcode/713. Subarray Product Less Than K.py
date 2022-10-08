# Link: https://leetcode.com/problems/subarray-product-less-than-k/solution/
# Q: 713. Subarray Product Less Than K
# Two pointer

# Time: O(N)
# Space: O(1)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, res, mult = 0, 0, 1
        
        if k == 0 or k == 1:
            return 0
        
        for r in range(n):
            mult *= nums[r]
            while mult >= k:
                mult /= nums[l]
                l += 1
            
            res += r - l + 1
        
        return res
            
            
