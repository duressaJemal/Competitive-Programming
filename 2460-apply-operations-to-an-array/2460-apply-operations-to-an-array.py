# Time: O(N)
# Space: O(1)

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        for index in range(n - 1):
            if nums[index] == nums[index + 1]:
                nums[index] *= 2
                nums[index + 1] = 0
        
        left = 0
        for right in range(n):
            if nums[right]:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums
        
        