class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        left = 0
        
        for right in range(n):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            
        
        