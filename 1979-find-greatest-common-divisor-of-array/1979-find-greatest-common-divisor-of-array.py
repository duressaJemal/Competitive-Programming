class Solution:
    def findGCD(self, nums: List[int]) -> int:

        
        mx = 0
        mn = 1001
        
        for val in nums:
            mx = max(mx, val)
            mn = min(mn, val)
        
        return gcd(mx, mn)
        
        