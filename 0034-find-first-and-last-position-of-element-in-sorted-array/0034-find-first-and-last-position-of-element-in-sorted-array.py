class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(target):
            n = len(nums)
            
            left = -1
            right = n # valid
            
            while right > left + 1:
                
                mid = left + (right - left) // 2
                
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid
            
            return right
        
        start = binary_search(target)
        end = binary_search(target + 1)

        if start >= len(nums) or nums[start] != target:
            return [-1, - 1]
        
        return [start, end - 1]
            
            