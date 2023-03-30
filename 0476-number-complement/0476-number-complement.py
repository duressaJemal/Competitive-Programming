class Solution:
    def findComplement(self, num: int) -> int:
        
        bit_mask = 1
        
        while bit_mask <= num:
            bit_mask = bit_mask << 1
        
        bit_mask -= 1
        num ^= bit_mask
        return num
        
        
        