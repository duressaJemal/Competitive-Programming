# Time: O(N)
# Space: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for right in range(n):
            
            while nums[right] != right + 1:
                
                temp = nums[right]
                if nums[right] != nums[temp - 1]:
                    nums[right],nums[temp - 1], = nums[temp - 1], nums[right]
                else:
                    break
        
        for index, value in enumerate(nums):
            if value != index + 1:
                return value
        