class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        
        def is_good(m):
            
            total = 0
            for rank in ranks:
                total += floor(sqrt(m/rank))
            
            return total >= cars
            
            
        right = 10 ** 14 # valid
        left = 0 # invalid
        
        while right > left + 1:
            
            mid = left + (right - left) // 2
            
            if is_good(mid):
                right = mid
            else:
                left = mid
        
        return right
            