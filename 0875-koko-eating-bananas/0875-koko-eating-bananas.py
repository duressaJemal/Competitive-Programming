class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def is_valid(k):
            hour_count = 0
            
            for value in piles:
                
                if k >= value:
                    hour_count += 1
                else:
                    hour_count += (ceil(value / k))

            return hour_count <= h
            
            
        total = max(piles)
        
        left = 0 # first invalid
        right = total # always valid
        
        while right > left + 1:
            
            mid = left + (right - left) // 2
            
            if is_valid(mid):
                right = mid
            else:
                left = mid
        
        return right
            