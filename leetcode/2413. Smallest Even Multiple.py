# Link: https://leetcode.com/problems/smallest-even-multiple/
#Q: 2413. Smallest Even Multiple

# Time: O(1)
# Space: O(1)

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        if n % 2 == 0:
            return n
        else:
            return n * 2
        
