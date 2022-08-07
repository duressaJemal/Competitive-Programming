# Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

# Binary search

# Time: O(N * log(N))
# Space:

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        n = len(weights)
        
        def is_good(x):
            index = 0
            for i in range(days):
                SUM = 0
                while index < n and (SUM + weights[index]) <= x:
                    SUM += weights[index]
                    index += 1
            return index == n
        
        left = -1 # first bad value
        right = 500 * n # first good value
        
        while right > left + 1:
            mid = (left + right) // 2
            if is_good(mid):
                right = mid
            else:
                left = mid
        return right
    
