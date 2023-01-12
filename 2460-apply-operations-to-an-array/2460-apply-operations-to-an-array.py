class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        for index in range(n - 1):
            if nums[index] == nums[index + 1]:
                nums[index] *= 2
                nums[index + 1] = 0
        
        
        write = 0
        
        for read in range(n):
            
            if not nums[read]:
                
                # find write index
                while write < read or (write < n and not nums[write]):
                    write += 1
                
                if write < n:
                    nums[read], nums[write] = nums[write], nums[read]
                else:
                    return nums
        
        return nums
        
        