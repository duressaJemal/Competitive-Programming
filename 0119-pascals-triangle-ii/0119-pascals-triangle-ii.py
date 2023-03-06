class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def solve(row):
            if not row:
                return [1]
            
            current_row = [1] * (row + 1)
            above_row = solve(row - 1)
            
            for index in range(1, row):
                current_row[index] = above_row[index - 1] + above_row[index]
            
            return current_row
        
        return solve(rowIndex)
        