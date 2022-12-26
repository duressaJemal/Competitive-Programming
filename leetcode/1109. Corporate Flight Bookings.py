# Link: https://leetcode.com/problems/corporate-flight-bookings/
#Q: 1109. Corporate Flight Bookings

# Time: O(N + M) where N = days, M = bookings
# Space: O(N)

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        range_sum = defaultdict(int)
        for left_bound, right_bound, value in bookings:
            range_sum[left_bound] += value
            range_sum[right_bound + 1] -= value
        
        output = []
        total = 0
        for i in range(1, n + 1):
            total += range_sum[i]
            output.append(total)
            
        return output
        
        
        
        
