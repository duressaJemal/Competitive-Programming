# Time: O(M*N)
# space: O(M*N)

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        def is_valid(row, col):
            if row < 0 or row >= row_len or col < 0 or col >= col_len:
                return False
            else:
                return True
            
        def dfs(row, col):
            
            # base case
            if board[row][col] == "M":
                board[row][col] = "X"
                return False
            
            visited.add((row, col))
            
            direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            
            if board[row][col] == "E":
                # find all adjecent mines
                count = 0
                for x, y in direction:
                    
                    nr = x + row
                    nc = y + col
                    
                    if is_valid(nr, nc) and board[nr][nc] == "M":
                        count += 1
                
                if count:
                    board[row][col] = str(count)
                else:
                    board[row][col] = "B"
            
            if board[row][col] == "B":

                for x, y in direction:
                    nr = x + row
                    nc = y + col
                    
                    if is_valid(nr, nc) and (nr, nc) not in visited: 
                        if not dfs(nr, nc):
                            return False
            
            return True
        
        row_len = len(board)
        col_len = len(board[0])
        visited = set()
        
        dfs(click[0], click[1])
        return board
        
                    
                    
                    

                
                
                
                
                
                
                
                
                
                
                
                
                
            
            