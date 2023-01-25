# Time: O(N)
# Space: O(N)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        for index in range(n):
            current_index = (index + k) % n
            prev_value = nums[index]
            
            if isinstance(prev_value, tuple):
                prev_value = prev_value[0]
            
            nums[current_index] = (nums[current_index], prev_value)
        
        for index, value in enumerate(nums):
            nums[index] = value[1]
        
        
        
            
        
            
            