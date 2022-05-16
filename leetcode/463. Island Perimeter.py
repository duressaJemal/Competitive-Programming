#link https://leetcode.com/problems/island-perimeter/submissions/
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        counter = 0
        visited = set()
        
        def dfs(r, c):
            
            nonlocal counter
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0:
                counter += 1
                return
        
            if (r, c) in visited:
                return
            
            visited.add((r, c))
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + d[0], c + d[1]
                dfs(nr, nc)
            
        flag = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    flag = True
                    break
            if flag == True:
                break
        
        dfs(i, j)
        return counter
