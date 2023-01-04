# Link: https://leetcode.com/problems/queens-that-can-attack-the-king/
#Q: 1222. Queens That Can Attack the King

# Time: O(N * 8) where 8 = directions of iteration and N = len(grid[0])
# Space: O(N)

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        direct_attack = []
        queens_location = set()
        
        for row, col in queens:
            queens_location.add((row, col))
            
        # directions for controlling the iteration (all 8 directions)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        
        for row, col in directions:
            
            current_row = king[0] + row
            current_col = king[1] + col
            
            while (0 <= current_row < 8) and (0 <= current_col < 8):
                if (current_row, current_col) in queens_location:
                    direct_attack.append([current_row, current_col])
                    break
                else:
                    current_row += row
                    current_col += col
        
        return direct_attack
                    
                
            
