class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res =[]
        
        for right in range(n):
            
            while nums[right] != right + 1:
                
                temp = nums[right]
                if nums[right] != nums[temp - 1]:
                    nums[right], nums[temp - 1] = nums[temp - 1], nums[right]
                else:
                    break
        
        for index, value in enumerate(nums):
            if value != index + 1:
                res.append(value)
                
        return res