class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        mn = 1
        for val in nums:
            mn = mn & val
        
        if mn:
            return 1
        
        count = 0
        reset = True
        current_value = 0
        
        for val in nums:
            
            if reset == True:
                current_value = val
                reset = False
                
            # add
            current_value = current_value & val
            
            if current_value == mn:
                count += 1
                reset = True
    
        return count or 1
        
        