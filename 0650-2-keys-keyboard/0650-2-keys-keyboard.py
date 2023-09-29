class Solution:
    def minSteps(self, n: int) -> int:
        
        def dp(num):
            if num == 1:
                return 0
            
            mn = float("inf")
            
            for i in range(1, num):
                if num % i == 0:
                    mn = min(mn, dp(i) + (num // i))
            
            return mn
        
        return dp(n)