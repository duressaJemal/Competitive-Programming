# Time: O(1)
# Space: O(1)

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        res = 0
        
        for row in range(m - 2):
            for col in range(n - 2):
                
                visited = set()
                r_sum = [0, 0, 0]
                c_sum = [0, 0, 0]
                l_digonal = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
                
                r_digonal = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]
                
                
                for r_n in range(row, row + 3):
                    for c_n in range(col, col + 3):
                        
                        cur = grid[r_n][c_n]
                        visited.add(cur)
                        r_sum[r_n - row] += cur
                        c_sum[c_n - col] += cur
                
                if len(set(r_sum)) == 1:
                    if r_sum == c_sum and r_sum[0] == l_digonal and r_sum[0] == r_digonal:
                        is_valid = True
                        for num in range(1, 10):
                            if num not in visited:
                                is_valid = False
                                break
                        
                        if is_valid:
                            res += 1
        
        return res
                    
                
                
                        
                        
                        