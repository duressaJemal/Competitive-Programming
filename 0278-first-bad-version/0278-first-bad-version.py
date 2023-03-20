# Time: O(log(N))
# Space: O(1)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 0
        right = n
        
        while right > left + 1:
            
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        
        return right