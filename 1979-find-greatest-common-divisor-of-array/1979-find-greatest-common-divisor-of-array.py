# Time: O(N)
# Space: O(1)

class Solution:
    def findGCD(self, nums: List[int]) -> int:
 
        mx = 0
        mn = 1001
        
        for val in nums:
            mx = max(mx, val)
            mn = min(mn, val)
        
        # gcd() returns greatest common divisor of two numbers
        return gcd(mx, mn)

        