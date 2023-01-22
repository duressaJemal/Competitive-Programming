# Time: O(log(N)) with base 10
# Space: O(1)

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        output = 0
        sign = 1
        
        while n:
            sign *= -1
            output += sign * (n % 10)
            n = n // 10
        
        return output * sign
    
    