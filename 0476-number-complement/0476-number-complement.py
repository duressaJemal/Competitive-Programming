class Solution:
    def findComplement(self, num: int) -> int:
        
        ln = int.bit_length(num)
        cur = (2 ** ln) - 1

        num ^= cur
        return num
        
        
        