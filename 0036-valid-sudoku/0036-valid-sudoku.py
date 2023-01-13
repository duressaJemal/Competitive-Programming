# Time: O(N^2) since N = 9, O(1)
# Space: O(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_len = len(board)
        col_len = row_len
        
        for row in range(row_len):
            unique = set()
            for col in range(col_len):
                if board[row][col] != "." and board[row][col] in unique:
                    return False
                unique.add(board[row][col])
        
        for col in range(col_len):
            unique = set()
            for row in range(row_len):
                if board[row][col] != "." and board[row][col] in unique:
                    return False
                unique.add(board[row][col])
        
        for row in range(0, 7, 3):
            for col in range(0, 7, 3):
                
                unique = set()
                
                for nr in range(row, row + 3):
                    for nc in range(col, col + 3):
                        if board[nr][nc] != "." and board[nr][nc] in unique:
                            return False
                        unique.add(board[nr][nc])
                
                        
        
        return True
                