class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        @cache
        def dp(l, search_cost, prev):
            
            # base case
            if l == 0:
                
                if search_cost == k:
                    return 1
                else:
                    return 0
            
            output = 0
            
            for val in range(1, m + 1):
                
                if val > prev:
                    output += dp(l - 1, search_cost + 1, val)
                else:
                    output += dp(l - 1, search_cost, prev)
                
            
            return output % MOD
        
        MOD = 10 ** 9 + 7
        return dp(n, 0, -1) % MOD
                    
            