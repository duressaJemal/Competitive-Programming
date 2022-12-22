# Link: https://leetcode.com/problems/largest-perimeter-triangle/
#Q: 976. Largest Perimeter Triangle

# Time: O(Nlog(N))
# Space: O(N) b/c sort() is O(N)

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < nums[i - 1] + nums[i - 2]:
                return nums[i] + nums[i - 1] + nums[i - 2]
        return 0
            
        
