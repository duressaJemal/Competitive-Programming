class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n == 2: return 1
        if n == 3: return 2
        if n == 4: return 4
        
        output = 1
        
        while n:
            if n <= 4:
                output *= n
                break
            else:
                output *= 3
                n -= 3
        
        return output
            
        