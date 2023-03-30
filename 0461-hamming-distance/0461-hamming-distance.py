class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        x ^= y
        ln = int.bit_length(x)
        
        bit_mask = 1
        bit_len = 1
    
        count = 0
        
        while bit_len <= ln:
            
            if (bit_mask & x) != 0:
                count += 1
            
            bit_mask = bit_mask << 1
            bit_len += 1
        
        return count
            