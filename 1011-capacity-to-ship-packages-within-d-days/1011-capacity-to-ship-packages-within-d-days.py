class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        def is_valid(limit):
            
            count_days = 0
            total_weights = 0
            
            for val in weights:
                
                if total_weights + val <= limit:
                    total_weights += val
                else:
                    count_days += 1
                    if val >= limit:
                        count_days += 1
                        total_weights = 0
                    else:
                        total_weights = val
                
                
            if total_weights <= limit:
                count_days += 1
            
            return count_days <= days
            
        
        max_weight = max(weights)
        
        right = max_weight * (5 * (10 ** 4))
        left = max_weight - 1 # assume invalid
        
        while right > left + 1:
            
            mid = left + (right - left) // 2
            
            if is_valid(mid):
                right = mid
            else:
                left = mid
        
        return right
        
        
        