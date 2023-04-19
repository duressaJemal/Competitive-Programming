# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def dfs(row, col):
            
            # base cases
            if row < 0 or row >= row_len or col < 0 or col >= col_len:
                return
            if board[row][col] != "O":
                return
            
            # mark visited and change value
            board[row][col] = "#"
            
            direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for x, y in direction:
                nr = x + row
                nc = y + col
                
                dfs(nr, nc)
            
            return
            
        
        row_len = len(board)
        col_len = len(board[0])

        for row in range(row_len):
            for col in range(col_len):
                # only for outer "0"
                if (row in [0, row_len - 1] or col in [0, col_len - 1]) and board[row][col] == "O":
                    dfs(row, col)
        
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"
        
