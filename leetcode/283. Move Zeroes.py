class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        start = 0
        for end in range(len(nums)):
            if nums[end] != 0:
                
                if nums[start] == 0:
                    nums[start] = nums[end]
                    nums[end] = 0
                    start += 1
                    continue
                    
                nums[start] = nums[end]
                start += 1
                
                
                
