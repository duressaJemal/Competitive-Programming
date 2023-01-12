class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        for index in range(n - 1):
            if nums[index] == nums[index + 1]:
                nums[index] *= 2
                nums[index + 1] = 0
        
        write = 0
        for read in range(n):
            if nums[read]:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1
        return nums
        
        