# Time: O(Mlog(N)) where M = len(weights), N = len(days)
# Space: O(1)

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        
        def is_valid(limit):
            
            days_count = 1
            total_weights = 0
            
            for val in weights:

                total_weights += val
                
                if total_weights > limit:
                    days_count += 1
                    total_weights = val

            return days_count <=days
            

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
        
        
        