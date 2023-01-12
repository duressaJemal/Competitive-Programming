class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        """
        movement = right, down, left, up
        set_bounds in the row(down, up) and col(right, left)
        
        after expanding in a given direction till reaching the bound
        update the bound and change direction
        
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        output = []
        
        directions = {"r": (0, 1), "l": (0, -1), "d": (1, 0), "u": (-1, 0)}
        
        row = 0
        col = -1
        
        right_bound = n
        left_bound = -1
        upper_bound = -1
        lower_bound = m
        
        number_of_operations = ceil(min(m, n) / 2)
        for operation in range(number_of_operations):
            
            # right direction
            nr = directions["r"][0]
            nc = directions["r"][1]
            
            while left_bound < col + nc < right_bound and upper_bound < row + nr < lower_bound:
                row += nr
                col += nc
                output.append(matrix[row][col])
            upper_bound = row
        
                
            # downward
            nr = directions["d"][0]
            nc = directions["d"][1]
            
            while upper_bound < row + nr < lower_bound and left_bound < col + nc < right_bound:
                row += nr
                col += nc
                output.append(matrix[row][col])
            right_bound = col
            
            
            # left directions
            nr = directions["l"][0]
            nc = directions["l"][1]
            
            while left_bound < col + nc < right_bound and upper_bound < row + nr < lower_bound:
                row += nr
                col += nc
                output.append(matrix[row][col])
            lower_bound = row
            
            
            # upward
            nr = directions["u"][0]
            nc = directions["u"][1]
            
            while upper_bound < row + nr < lower_bound and left_bound < col + nc < right_bound:
                row += nr
                col += nc
                output.append(matrix[row][col])
            left_bound = col

        return output
            
            
            
            
                
        
        
        
        