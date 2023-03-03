# Time: O(log3(N))
# space: O(log3(N))

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n < 3:
            return n == 1
        
        return self.isPowerOfThree(n / 3)