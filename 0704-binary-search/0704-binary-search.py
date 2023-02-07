class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        left = -1
        right = n - 1
        
        while right > left + 1:
            mid = (left + right) // 2
            
            if target <= nums[mid]:
                right = mid
            else:
                left = mid
            

        if target == nums[right]:
            return right
        else:
            return - 1