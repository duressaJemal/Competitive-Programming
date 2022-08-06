# Link: https://leetcode.com/problems/search-a-2d-matrix/

# Binary search -- Brute

# Time: O(N * log(max - min))
# Space: O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        start, end = matrix[0][0], matrix[m - 1][n - 1]
        
        def count_smaller(mid, m, n):
            row, col = m - 1, 0
            smaller_count = 0
            
            while row >= 0 and col < n:
    
                if matrix[row][col] > mid:
                    bound[1] = min(bound[1], matrix[row][col])
                    row -= 1
                else:
                    bound[0] = max(bound[0], matrix[row][col])
                    smaller_count += 1
                    col += 1
                    
            return smaller_count
            
        while start < end:
            
            mid = start + (end - start) // 2
            
            bound = [matrix[0][0], matrix[m - 1][n - 1]]
            count = count_smaller(mid, m, n)
            
            if target <= mid:
                end = bound[0]
            if target > mid:
                start = bound[1]
        
        if start == target or end == target:
            return True
        
        return False
    
    
    
# Binary search -- optimal

# Time: O(log(M * N))
# Space:n O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        start, end = 0, m * n - 1
        
        while start < end:
            mid = start + (end - start) // 2
            if matrix[mid//n][mid%n] < target:
                start = mid + 1
            else:
                end = mid
                
        return matrix[start // n][start % n] == target

                
            
            
