# Link: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
#Q: 2482. Difference Between Ones and Zeros in Row and Column

# Time: O(M*N)
# Space: O(M + N)

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        
        row_count = {}
        col_count = {}
        
        # precalculate the number of ones and zeros in each row
        for row in range(m):
            
            ones = 0
            zeros = 0
            for col in range(n):
                if grid[row][col] == 1:
                    ones += 1
                else:
                    zeros += 1
            row_count[row] = [zeros, ones]
        
        # precalculate the number of ones and zeros in each column
        for col in range(n):
            
            ones = 0
            zeros = 0
            
            for row in range(m):
                if grid[row][col] == 1:
                    ones += 1
                else:
                    zeros += 1
                    
            col_count[col] = [zeros, ones]
        
        for i in range(m):
            for j in range(n):
                
                grid[i][j] = (row_count[i][1] + col_count[j][1]) - (row_count[i][0] + col_count[j][0])
                
        return grid
    
    
# From discuss section

# Time: O(M*N)
# Space: O(M + N)

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
      
        m = len(grid)
        n = len(grid[0])
        
        row = [0] * m
        col = [0] * n
        
        for i in range(m):
            for j in range(n):
                row[i] += grid[i][j]
                col[j] += grid[i][j]
                
        for i in range(m):
            for j in range(n):
                grid[i][j] = (row[i] + col[j]) - (m - row[i]) - (n - col[j])
        
        return grid
                
    
       
