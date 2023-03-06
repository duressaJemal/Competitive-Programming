# Time: O(Nlog(N))
# Space: O(1)

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def is_valid(divisor):
            
            total = 0
            for val in nums:
                total += ceil(val / divisor)
            
            return total <= threshold
        
        left = 0 # invalid
        right = max(nums) + 1
        
        while right > left + 1:
            
            mid = left + (right - left) // 2
            
            if is_valid(mid):
                right = mid
            else:
                left = mid
        
        return right
        