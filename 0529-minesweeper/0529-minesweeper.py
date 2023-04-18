class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def count_adjecent(row, col):
            
            count = 0
            direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

            for x, y in direction:
                nr = x + row
                nc = y + col
                
                if not (nr < 0 or nr >= row_len or nc < 0 or nc >= col_len): # if valid cell
                    if board[nr][nc] == "M":
                        count += 1
                        
            return count
            
        def dfs(row, col):
            
            # base case
            if board[row][col] == "M":
                board[row][col] = "X"
                return False
            
            visited.add((row, col))
            
            if board[row][col] == "E":
                # find all adjecent mines
                count = count_adjecent(row, col)
                
                if count:
                    board[row][col] = str(count)
                else:
                    board[row][col] = "B"
            
            if board[row][col] == "B":
                direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
                for x, y in direction:
                    nr = x + row
                    nc = y + col
                    
                    if not (nr < 0 or nr >= row_len or nc < 0 or nc >= col_len) and (nr, nc) not in visited: 
                        if not dfs(nr, nc):
                            return False
            
            return True
        
        row_len = len(board)
        col_len = len(board[0])
        visited = set()
        
        dfs(click[0], click[1])
        return board
        
                    
                    
                    

                
                
                
                
                
                
                
                
                
                
                
                
                
            
            