# Heap

# Time: O(k * log(N))  -- in the worst case k == N^2
# Space: O(N^2)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = [element for row in matrix for element in row]
        heapify(heap)

        while k:
            
            if k == 1:
                return heappop(heap)
            
            heappop(heap)
            k -= 1
      
    
# Binary search

# Time: O(N * log(max - min))
# Space: O(1)
    
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        def count_larger_smaller(matrix, mid, bound):
            
            smaller_count = 0
            n = len(matrix)
            row, col = len(matrix) - 1, 0
            
            while row >= 0 and col < n:
                
                if matrix[row][col] > mid:
                    bound[1] = min(bound[1], matrix[row][col])
                    row -= 1
                
                else:
                    bound[0] = max(bound[0], matrix[row][col])
                    smaller_count += row + 1
                    col += 1
            
            return (smaller_count, bound)
        
        
        start, end = matrix[0][0], matrix[m - 1][n - 1]
        
        while start < end:
            
            bound = [matrix[0][0], matrix[m - 1][n - 1]]
            mid = start + (end - start) // 2

            count, bound = count_larger_smaller(matrix, mid, bound)
            if count == k:
                return bound[0]
            elif count < k:
                start = bound[1]
            else:
                end = bound[0]
        
        return start
                
