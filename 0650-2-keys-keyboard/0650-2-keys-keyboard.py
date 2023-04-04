# Time: O(N)
# Space: O(1)

class Solution:
    def minSteps(self, n: int) -> int:
        
        len_left = n - 1
        cur_length = 1
        
        operations = 0
        copy_length = 1
        
        while len_left:
            
            # if the undivided segemnt can be divided equally with cur_length
            if len_left % cur_length == 0: 

                operations += 2
                len_left -= cur_length
                copy_length = cur_length
                cur_length *= 2
                
            else:
                
                # for copying
                if copy_length == cur_length:
                    operations += 1
                    
                # for pasting 
                operations += 1
                len_left -= copy_length
                cur_length += copy_length
                
        
        return operations
