class Solution:
    def monkeyMove(self, n: int) -> int:
        
        def power(n, a, mod):
            if n == 0:
                return 1
            elif n == 1:
                return a
            
            res = power(n // 2, a, mod)
    
            if n % 2 == 0:
                return ((res % mod) * (res % mod)) % mod
            else:
                return ((res % mod) * a * (res % mod)) % mod
            
        mod = 10 ** 9 + 7  
        return (power(n, 2, mod) - 2) % mod


