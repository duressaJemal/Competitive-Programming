# Link: https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
#Q: 2279. Maximum Bags With Full Capacity of Rocks

# Time: O(Nlog(N))
# Space: O(N)

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        n = len(capacity)
        gap = [0] * n
        
        for i in range(n):
            gap[i] = capacity[i] - rocks[i]
        
        gap.sort()
        total, count = 0, 0
        
        for current in gap:
            if (total + current) <= additionalRocks:
                total += current
                count += 1
            else:
                break
        
        return count
