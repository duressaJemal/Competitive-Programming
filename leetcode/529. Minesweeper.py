# Link: https://leetcode.com/problems/minesweeper/

# DFS

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        m = len(board)
        n = len(board[0])
        
        def dfs(r, c):
            
            if r < 0 or c < 0 or r >= m or c >= n:
                return False
            
            if board[r][c] == "M":
                board[r][c] = "X"
                return True
                
            if board[r][c] != "E":
                return False
            
            count = 0
            for dirc in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                nr = r + dirc[0]
                nc = c + dirc[1]
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                if board[nr][nc] == "M":
                    count += 1
            board[r][c] = str(count) if count else "B"
            

            if board[r][c] == "B":
                found = False
                for dirc in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    nr = r + dirc[0]
                    nc = c + dirc[1]
                    
                    if found:
                        return True
                    
                    found = found or dfs(nr, nc)
                    
        dfs(click[0], click[1])
        return board
