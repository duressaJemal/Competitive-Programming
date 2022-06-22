# link: https://leetcode.com/problems/last-stone-weight/submissions/

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1: return stones[0]
        
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
        
            if y != x:
                heapq.heappush(heap, x - y)
            
        if len(heap) == 0: return 0
        return -heap[0]
        
        
        
        
