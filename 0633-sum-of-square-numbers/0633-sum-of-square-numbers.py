# Time: O(sqrt(N))
# Space: O(1)

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
            
        left = 0
        right = ceil(sqrt(c))
        
        while left <= right:
            value = left * left + right * right
            
            if value == c:
                return True
            elif value < c:
                left += 1
            else:
                right -= 1
        
        return False