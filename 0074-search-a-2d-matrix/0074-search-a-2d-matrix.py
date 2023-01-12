# binary search

# Time: O(log(M*N))
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
                