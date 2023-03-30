# Time: O(Nlog(N)) 
# Space: O(1)

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        x ^= y
        
        bit_mask = 1
        count = 0
        
        while int.bit_length(bit_mask)<= int.bit_length(x):
            
            if (bit_mask & x) != 0:
                count += 1
            bit_mask = bit_mask << 1
            
        return count
            