# link: https://leetcode.com/problems/surrounded-regions/

# DFS

# time: O(m*n)
# space: O(m*n)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])
        
        def dfs(r, c):
            
            if r < 0 or c < 0 or r == m or c == n or board[r][c] != "O": 
                return
            
            board[r][c] = "#"
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for row in range(m):
            for col in range(n):

                if board[row][col] == "O" and (row in [0, m - 1] or col in [0, n - 1]):
                    dfs(row, col)

        for row in range(m):
            for col in range(n):
                
                if board[row][col] == "O":
                    board[row][col] = "X"
                    
        for row in range(m):
            for col in range(n):
                
                if board[row][col] == "#":
                    board[row][col] = "O"
                    

        
# BFS 

# time: O(m*n)
# space: O(m*n)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m = len(board)
        n = len(board[0])
        count = 0
        queue = deque([])
                    
        for row in range(m):
            for col in [0 ,n - 1]:
                if board[row][col] == "O":
                    board[row][col] = "#"
                    queue.append((row, col))
        
        for row in [0, m - 1]:
            for col in range(1, n - 1):
                if board[row][col] == "O":
                    board[row][col] = "#"
                    queue.append((row, col))
        
        while queue:
            
            row, col = queue.popleft()
            
            for dirc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = row + dirc[0]
                nc = col + dirc[1]
                
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                
                if board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    queue.append((nr, nc))
                
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == "#":
                    board[row][col] = "O"
   
