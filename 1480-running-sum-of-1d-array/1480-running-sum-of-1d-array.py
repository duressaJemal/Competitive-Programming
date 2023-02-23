# Time: O(N)
# Space: O(1)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        for index in range(1, n):
            nums[index] += nums[index - 1]
        
        return nums
        
        