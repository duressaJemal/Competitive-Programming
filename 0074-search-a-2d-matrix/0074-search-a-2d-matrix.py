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
        
        