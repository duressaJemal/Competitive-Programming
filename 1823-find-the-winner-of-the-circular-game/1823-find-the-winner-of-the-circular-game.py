# Time: O(N^2)
# Space: O(N)

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        nums = list(range(1, n + 1))
        
        current_index = 0
        
        while len(nums) > 1:
            remove_index = (current_index + k - 1) % len(nums)
            nums.pop(remove_index)
            current_index = remove_index % len(nums)
        
        return nums[0]


        
        
    
        
        
        