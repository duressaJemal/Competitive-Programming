class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        n = len(image)
        m = len(image[0])
        original_color = image[sr][sc]
        visited = set()
        
        def dfs(r, c):
            
            image[r][c] = newColor
            visited.add((r,c))
            
            for direction in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                new_row  = r + direction[0]
                new_col = c + direction[1]
                
                if (new_row, new_col) not in visited and 0 <= new_row < n and 0 <= new_col < m and image[new_row][new_col] == original_color:
                    dfs(new_row, new_col)
                
        dfs(sr, sc)
        
        return image
