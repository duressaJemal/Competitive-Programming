# Link: https://leetcode.com/problems/minimum-time-to-complete-trips/

# Binary search

# Time: O(N * log(max)) -- where max == 10 ** 14
# Space: O(1)

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def is_good(limit):
            total = 0
            for t in time:
                total += limit//t
            return total >= totalTrips

        left = 0 # first bad value
        right = 10 ** 14 # first right value
        
        while right > left + 1:
            
            mid = (left + right) // 2
            if is_good(mid):
                right = mid
            else:
                left = mid
            
        return right
        
        
