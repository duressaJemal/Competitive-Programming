# link: https://leetcode.com/problems/flood-fill/submissions/

# DFS

# time: O(n*m)
# space: O(n*m)

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
            
        
        
# BFS

# time: O(n*m)
# space: O(n*m)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        old_color = image[sr][sc]
        queue = deque([(sr, sc)])
        
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        if image[sr][sc] == color: return image
        
        while queue:
            
            r, c = queue.popleft()
            image[r][c] = color
            
            for dirc in direction:
                
                nr = r + dirc[0]
                nc = c + dirc[1]
                
                if nr < 0 or nr >= m or nc < 0 or nc >= n: continue
                if image[nr][nc] != old_color: continue
                    
                queue.append((nr, nc))
            
        return image
        
            
            
            
