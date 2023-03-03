class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def predictor(left, right):
            
            if left == right:
                return nums[left]
            
            pick_left = nums[left] - predictor(left + 1, right)
            pick_right = nums[right] - predictor(left, right - 1)
            
            return max(pick_left, pick_right)
        
        return predictor(0, len(nums) - 1) >= 0
        