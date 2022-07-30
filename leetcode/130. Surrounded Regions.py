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
                    

        
# BFS --- TLE

# time: O(m*n)
# space: O(m*n)

# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
        
#         m = len(board)
#         n = len(board[0])
        
#         visited = set()
        
#         def bfs(r, c):
            
#             queue = deque([(r, c)])
            
#             while queue:
                
#                 row, col = queue.popleft()
#                 board[row][col] = "#"
                
#                 for dirc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                     nr = row + dirc[0]
#                     nc = col + dirc[1]
                    
#                     if nr < 0 or nc < 0 or nr >= m or nc >= n or board[nr][nc] != "O" or (r, c) in visited:
#                         continue
                    
#                     queue.append((nr, nc))
#                     visited.add((nr, nc))
                    
                    
#         for row in range(m):
#             for col in range(n):
                
#                 if board[row][col] == "O" and (row in [0, m - 1] or col in [0, n - 1]):
#                     bfs(row, col)
        
#         for row in range(m):
#             for col in range(n):
                
#                 if board[row][col] == "O":
#                     board[row][col] = "X"
                    
#         for row in range(m):
#             for col in range(n):
                
#                 if board[row][col] == "#":
#                     board[row][col] = "O"
    

        
