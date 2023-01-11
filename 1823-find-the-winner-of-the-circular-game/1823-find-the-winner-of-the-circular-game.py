class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        """
        start from current
        
        
        500 * 500 = 250, 000
        
        current_index = 
        
        1, 2, 3, 4, 5,
        
        4 % 4 = 0
        
        if it was on 0 then it will be on 0
        but if to the right:
            
          
        current_index = (current_index + k) % len(array)
        remove from current_index
        then calibrate the new index
            new_index = current_index % len(array)
        
        """
        
        nums = list(range(1, n + 1))
        
        current_index = 0
        
        while len(nums) > 1:
            remove_index = (current_index + k - 1) % len(nums)
            nums.pop(remove_index)
            current_index = remove_index % len(nums)
        
        return nums[0]
    
        
        
        
    
        
        
        