# binary search

# Time: O(log(M*N))
# Space: O(1)

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
#         for row in matrix:
            
#             is_found = False
            
#             # do binary search
            
#             left = -1
#             right = len(row) - 1
            
#             while left + 1 < right:
                
#                 mid = (left + right) // 2
#                 if target > row[mid]:
#                     left = mid
#                 elif target < row[mid]:
#                     right = mid
#                 else:
#                     is_found = True
#                     break
            
#             if is_found or row[right] == target:
#                 return True
        
#         return False
                
# optimized

# Time: O(M + N)
# Space: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        """
        
        start from the top
        go to down or right:
            if current grid is the value:
                return True
                
            if larger or equal to downward value:
                go downward:
            elif >= right value:
                go to the right
            else:
                return False
        
        how to implement it?
        
        iterate over M + N:
            and hold current_row and current_column
            if there is way to move to left or down:
                pass
            else:
                we have reached the last element
                
            if there is no way to move downward:
                move to the right
            
            if there is no way to move righwards:
                move downward
            
            
        """
        
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
        
        
                
                
                    
                
                
                
                
        
        
        
        
        
        
        
        