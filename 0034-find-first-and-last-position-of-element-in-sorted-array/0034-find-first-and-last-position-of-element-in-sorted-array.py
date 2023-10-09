class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left_index = bisect.bisect_left(nums, target)
        right_index = bisect.bisect_right(nums, target)
        
        
        if left_index < len(nums) and nums[left_index] == target:
            return [left_index, right_index - 1]
        else:
            return [-1, -1]
        