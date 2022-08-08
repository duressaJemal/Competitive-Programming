# Link: https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

# Binary search

# Time: O(M * log(M*N)) -- wher M = row number, N = column
# Space: O(1)

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def is_good(number):
            count = 0
            for row in range(1, m + 1):
                count += min(number // row, n)
            return count >= k
        
        left = 0 # first bad value
        right = m * n  # first good value
        
        while right > left + 1:
            
            mid = (left + right) // 2
            if is_good(mid):
                right = mid
            else:
                left = mid
        
        return right
        
