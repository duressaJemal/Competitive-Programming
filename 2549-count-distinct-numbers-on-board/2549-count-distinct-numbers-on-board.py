# Time: O(1)
# Space: O(1)

class Solution:
    def distinctIntegers(self, n: int) -> int:
        
        if n == 1:
            return 1
        else:
            return n - 1