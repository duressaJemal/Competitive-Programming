# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# heap
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        heap = []
        
        for i in range(n):
            for j in range(n):
                heapq.heappush(heap, matrix[i][j])
        
        while k:
            
            if k == 1:
                return heapq.heappop(heap)
            
            heapq.heappop(heap)
            k -= 1
        
        

