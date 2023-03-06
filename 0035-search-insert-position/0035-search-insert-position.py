class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        left = -1 # assume invalid
        right = n # valid
        
        while right > left + 1:
            
            mid = left + (right - left) // 2
            
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        
        return right
    