class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        
        min_len = float("inf")
        current_sum = 0
        
        left = 0
        
        for right in range(n):
            # add
            current_sum += nums[right]
            
            # validate
            while current_sum - nums[left] >= target:
                current_sum -= nums[left]
                left += 1
            
            if current_sum >= target:
                min_len = min(min_len, right - left + 1)
        
        return 0 if min_len == float("inf") else min_len
            