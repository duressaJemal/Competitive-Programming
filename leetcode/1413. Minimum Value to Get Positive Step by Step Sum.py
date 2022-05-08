class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        minimum = min(nums)
        
        return 1 if minimum >= 1 else 0 - minimum + 1
    
