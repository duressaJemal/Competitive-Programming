# Time: O(Nlog(N))
# Space: O(1)

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        nums.sort()
        
        result = 0
        
        left = 0
        right = n - 1
        
        while left < right:
            current = nums[left] + nums[right]
            if current == k:
                left += 1
                right -= 1
                result += 1
            elif current < k:
                left += 1
            else:
                right -= 1
            
        
        return result
            
            