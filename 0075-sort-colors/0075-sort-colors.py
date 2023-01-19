class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        for index in range(1, n):
            if nums[index] < nums[index - 1]:
                for i in range(index, 0, -1):
                    if nums[i] < nums[i - 1]:
                        nums[i], nums[i - 1] = nums[i - 1], nums[i]
                    else:
                        break
        
                        
        
        