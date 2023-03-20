# Time: O(log(N)) 
# Space: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 0
        right = x + 1
        
        while right > left + 1:
            
            mid = left + (right - left) // 2
            
            res = mid * mid
            
            if res <= x:
                left = mid
            else:
                right = mid
        
        return left