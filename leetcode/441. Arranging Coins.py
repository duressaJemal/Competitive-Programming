# Link: https://leetcode.com/problems/arranging-coins/

# Binary search

# Time: O(log(N))
# Space: O(1)

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        left = 1
        right = n # assume false
        
        while right > left + 1:
            mid = (left + right) // 2
            if mid * (mid + 1) // 2 <= n:
                left = mid
            else:
                right = mid
        
        return left
        
        
