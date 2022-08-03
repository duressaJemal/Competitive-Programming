# Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Heap

# Time: O(k * log(N))  -- in the worst case k == N^2
# Space: O(n^2)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = [element for row in matrix for element in row]
        heapify(heap)

        while k:
            
            if k == 1:
                return heappop(heap)
            
            heappop(heap)
            k -= 1
        
