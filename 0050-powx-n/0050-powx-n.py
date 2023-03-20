class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def auxilary(x, n):
            
            if n == 0:
                return 1
            
            if x == 0:
                return 0
            
            ret = auxilary(x, n//2)
            ret = ret * ret
            
            if n % 2 == 0:
                return ret
            return x * ret
                     
        ret = auxilary(x, abs(n)) 
        
        if n > 0:
            return ret
        else:
            return 1/ret
                     


                     
                     
        
            
            
            
    
    