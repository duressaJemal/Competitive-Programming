# Link: https://leetcode.com/problems/furthest-building-you-can-reach/

# Time: O(N * log(N))
# Space: O(N)

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        n = len(heights)
        heap = []
        
        for i in range(n - 1):
            jump = heights[i + 1] - heights[i]
            
            if jump > 0:
                heappush(heap, jump)
                if len(heap) > ladders:
                    bricks -= heappop(heap)
                if bricks < 0:
                    return i
        
        return n - 1

    
