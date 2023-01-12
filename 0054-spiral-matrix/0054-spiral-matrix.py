# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])
        
        output = []
        
        row = 0
        col = -1
        
        right_bound = n
        left_bound = -1
        upper_bound = -1
        lower_bound = m
        
        number_of_operations = ceil(min(m, n) / 2)
        for operation in range(number_of_operations):
            
            # right direction
            nc = 1
            while col + nc < right_bound and upper_bound < row < lower_bound:
                col += nc
                output.append(matrix[row][col])
            upper_bound = row
        
            # downward
            nr = 1
            while row + nr < lower_bound and left_bound < col < right_bound:
                row += nr
                output.append(matrix[row][col])
            right_bound = col
            
            # left directions
            nc = -1
            while left_bound < col + nc and upper_bound < row < lower_bound:
                col += nc
                output.append(matrix[row][col])
            lower_bound = row
            
            # upward
            nr = -1
            while upper_bound < row + nr and left_bound < col < right_bound:
                row += nr
                output.append(matrix[row][col])
            left_bound = col

        return output
            
            
            
            
                
        
        
        
        