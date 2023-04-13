class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        old_color = image[sr][sc]
        visited = set()
        
        def dfs(image, r, c):
            
            if r < 0 or r >= m or c < 0 or c >= n: return 
            if image[r][c] != old_color: return
            if (r, c) in visited: return
            
            visited.add((r, c))
            image[r][c] = color
            
            dfs(image, r - 1, c)
            dfs(image, r + 1, c)
            dfs(image, r, c - 1)
            dfs(image, r, c + 1)
            
        
        dfs(image, sr, sc)
        return image