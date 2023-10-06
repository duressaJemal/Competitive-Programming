class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n <= 3:
            return n - 1
        
        output = 1
        
        while n:
            if n <= 4:
                output *= n
                break
            else:
                output *= 3
                n -= 3
        
        return output
            
        