# link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# time: O(n * 2)
# space: O(n * 2)

# heap
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = [element for row in matrix for element in row]
        heapq.heapify(heap)

        while k:
            
            if k == 1:
                return heapq.heappop(heap)
            heapq.heappop(heap)
            k -= 1
        

