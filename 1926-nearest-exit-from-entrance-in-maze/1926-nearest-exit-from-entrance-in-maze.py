# Time: O(V + E)
# Space: O(V)

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
                
        def is_valid(row, col):
            if 0 <= row < row_len and 0 <= col < col_len and maze[row][col] != "+":
                return True
            else:
                return False
        
        def in_boarder(row, col):
            if row in [0, row_len - 1] or col in [0, col_len - 1]:
                return True
            else:
                return False
            
        queue = deque([(entrance[0], entrance[1])])
        row_len, col_len = len(maze), len(maze[0])

        dirc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        
        level = 0
        while queue:
            
            n = len(queue)
            for _ in range(n):
                
                row, col = queue.popleft()
                if maze[row][col] == "." and in_boarder(row,col) and (row, col) != (entrance[0], entrance[1]):
                    return level
                
                for x, y in dirc:
                    nr = x + row
                    nc = y + col
                    
                    if is_valid(nr, nc):
                        if (nr, nc) not in visited:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                
            level += 1
        
        return -1
                    
                    
                
                
                