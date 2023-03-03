# Time: O(log4(N))
# Space: O(1)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n < 4:
            return n == 1
        
        return self.isPowerOfFour(n / 4)
    
    
        