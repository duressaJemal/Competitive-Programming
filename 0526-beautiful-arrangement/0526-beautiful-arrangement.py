# Time: O(K) where K is valid permutation
# Space: O(N)

class Solution:
    def countArrangement(self, n: int) -> int:
        
        def backtrack(bit, count):
            
            if count == n:
                res[0] += 1
                return
            
            for index in range(n):
                value = index + 1
                pos = count + 1
                
                # if valid to include the current value
                if (bit & (1 << index)) == 0 and (not (value % pos) or (not (pos % value))):
                    # on
                    bit = bit | (1 << index)
                    backtrack(bit, count + 1)
                    
                    # off
                    bit = bit ^ (1 << index)
        
        res = [0]
        backtrack(0, 0)
        
        return res[0]
        
        
        
                
                
                    
                
        