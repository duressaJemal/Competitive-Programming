# Link: https://leetcode.com/problems/last-stone-weight/

# Time: O(N * log(N))
# Space: O(N)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1: return stones[0]
        
        heap = [-stone for stone in stones]
        heapify(heap)
        
        while len(heap) > 1:
            
            y = -heappop(heap)
            x = -heappop(heap)
        
            if y != x:
                heappush(heap, x - y)
        
        return -heap[0] if heap else 0

        
