class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        """
        use two pointer(l, r)
        l = 0
        r = sqrt(c)
        
        approach: colliding pointers
        
        
        """
        
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