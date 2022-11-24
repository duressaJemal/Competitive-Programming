# Link: https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
#Q: 1509. Minimum Difference Between Largest and Smallest Value in Three Moves

# Time: O(Nlog(N))
# Space: O(1)

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        nums.sort()
        
        if len(nums) < 4: return 0
        return min(nums[-3] - nums[1], nums[-4] - nums[0], nums[-1] - nums[3], nums[-2] - nums[2])
