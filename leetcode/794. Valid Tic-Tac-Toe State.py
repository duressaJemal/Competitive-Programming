# Link: https://leetcode.com/problems/valid-tic-tac-toe-state/
#Q: 794. Valid Tic-Tac-Toe State

# Time: O(N) where N = total number of elements in the given grid
# Space: O(N)

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        row_len = len(board)
        col_len = len(board[0])
        
        count = defaultdict(int)
        
        for row in range(row_len):
            for col in range(col_len):
                count[board[row][col]] += 1
                
        all_combinations = set()

        # generate all row combinations:
        for row in range(3):
            all_combinations.add(board[row])
        
        # generate all column combinations
        for col in range(3):
            vertical = ""
            for row in range(3):
                vertical += board[row][col]
            all_combinations.add(vertical)
        
        # generate all digonal combinations
        left_digonal = board[0][0] + board[1][1] + board[2][2]
        right_digonal = board[0][2] + board[1][1] + board[2][0]
        
        all_combinations.add(left_digonal)
        all_combinations.add(right_digonal)

        if (count["O"] > count["X"]) or (count["X"] > (count["O"] + 1)): 
            return False
        elif "X" * row_len in all_combinations and (count["O"] >= count["X"]):
            return False
        elif "O" * row_len in all_combinations and (count["O"] != count["X"]):
            return False
        
        return True
            
            
            
            
            
            
