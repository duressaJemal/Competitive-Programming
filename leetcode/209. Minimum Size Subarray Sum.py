# Link: https://leetcode.com/problems/minimum-size-subarray-sum/
#Q: 209. Minimum Size Subarray Sum

# Time: O(N)
# Space: O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l, res = 0, float("inf")
        x = 0
        
        for r in range(len(nums)):
            x += nums[r]
            while x >= target:
                x -= nums[l]
                l += 1
            
            if l != 0:
                res = min(res, r - l + 2)
        
        return 0 if res == float("inf") else res
    

# Smart solution with O(N*log(N)) :)
# prefix and binary search
