# Binary search

# Time: O(log(M*N))
# Space: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m * n
        
        while left + 1 < right:
            
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                left = mid
            else:
                right = mid
            
        return target == matrix[left // n][left % n]
    
# binary search

# Time: O(M*log(N))
# Space: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            
            is_found = False
            
            # do binary search
            
            left = -1
            right = len(row) - 1
            
            while left + 1 < right:
                
                mid = (left + right) // 2
                if target > row[mid]:
                    left = mid
                elif target < row[mid]:
                    right = mid
                else:
                    is_found = True
                    break
            
            if is_found or row[right] == target:
                return True
        
        return False
                
# optimized

# Time: O(M + N)
# Space: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        row = 0
        col = 0
        
        for operation in range(m + n):
            
            # if either is valid
            if row < m and col < n:
                
                if target == matrix[row][col]:
                    return True
                
                if row + 1 < m and target >= matrix[row + 1][col]:
                    row += 1
                elif col + 1 < n and target >= matrix[row][col + 1]:
                    col += 1
                else:
                    return False
        
        

                
                    
                
                
                
                
        
        
        
        
        
        
        
        