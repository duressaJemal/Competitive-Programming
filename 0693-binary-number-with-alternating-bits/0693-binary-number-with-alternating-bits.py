# Time: O(log(N))
# Space: O(1)

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        bit_mask = 1 if n & 1 != 0 else 0 # check if even or odd
        while n:
            if (bit_mask ^ n) & 1 != 0:
                return False
            bit_mask = 1 - bit_mask
            n = n >> 1
        return True
    
