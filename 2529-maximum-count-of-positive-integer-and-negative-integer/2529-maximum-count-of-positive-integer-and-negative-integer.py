class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        negative_nums = bisect_left(nums, 0)
        positive_nums = len(nums) - bisect_right(nums, 0)
        
        return max(negative_nums, positive_nums)
        
        
    