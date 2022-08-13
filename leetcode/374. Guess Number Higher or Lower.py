# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# Link: https://leetcode.com/problems/guess-number-higher-or-lower/

# Binary search

# Time: O(N)
# Space: O(1)

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left = 0
        right = 2 ** 31
        
        while right > left + 1:
            mid = (right + left) // 2
            if guess(mid) == -1:
                right = mid
            else:
                left = mid
                
        return left
            
            
