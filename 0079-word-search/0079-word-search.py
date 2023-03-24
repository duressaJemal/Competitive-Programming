class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        
        def dfs(r, c, index):

            if word[index] != board[r][c]: return False
            if index == len(word) - 1:
                if word[index] == board[r][c]: return True
                else: return False
            
            dirc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            cur = False
            
            for x, y in dirc:
                
                nr = r + x
                nc = c + y
                
                if (nr, nc) not in visited:
                    
                    if not (nr < 0 or nr >= m or nc < 0 or nc >= n): 
                        # add
                        visited.add((nr, nc))
                        cur = cur or dfs(nr, nc, index + 1)
                        # remove
                        visited.remove((nr, nc))
                        
            return cur
        
        res = False
        visited = set()
        
        for row in range(m):
            for col in range(n):
                visited.add((row, col))
                res = res or dfs(row, col, 0)
                visited.remove((row, col))
                if res:
                    return True
        
        return False
                
            