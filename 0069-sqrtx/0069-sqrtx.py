class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = 1 # the min value it could be
        r = 2 ** 16
        print(r)
             
        while r > l + 1:
            mid = (l + r) // 2
            squared = mid * mid
            
            if squared < x:
                l = mid
            elif squared > x:
                r = mid
            else:
                return mid
        
        return l if x else 0