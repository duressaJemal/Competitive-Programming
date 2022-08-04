# Link: https://leetcode.com/problems/first-bad-version/

# Time: O(log(N))
# Space: (1)


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        
        first_bad = 1
        low, high = 1, n
        
        while low <= high:
            
            mid  = low + (high - low) // 2
            
            if isBadVersion(mid):
                first_bad = mid
                high = mid - 1
            
            else:
                low = mid + 1
            
        return first_bad
        

            
