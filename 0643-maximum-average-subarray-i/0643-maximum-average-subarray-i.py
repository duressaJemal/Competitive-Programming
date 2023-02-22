class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        left = 0
        
        max_sum = float("-inf")
        current_sum = 0
        
        for right in range(n):
            
            # add
            current_sum += nums[right]
            
            # is_valid
            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                
                # remove
                current_sum -= nums[left]
                left += 1
            
        
        return max_sum / k
            