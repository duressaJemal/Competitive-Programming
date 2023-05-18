class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        def valid_cell(row, col):
            if 0 <= row < row_len and 0 <= col < col_len:
                return True
            else:
                return False
        
        def valid_path(start, end, index):
            
            start_val = grid[start[0]][start[1]]
            end_val = grid[end[0]][end[1]]
            
            if start_val not in able_to_move[index]:
                return False
            
            if end_val not in accessible[index]:
                return False
            
            return True
                   
            
        def find(node):
            
            p = node
            while parent[node] != node:
                node = parent[node]
            
            while p != node:
                cur_parent = parent[p]
                parent[p] = node
                p = cur_parent
            
            return node
        
        def union(node1, node2):
            
            p_node1 = find(node1)
            p_node2 = find(node2)
            
            if p_node1 == p_node2:
                return 
            
            if rank[p_node1] > rank[p_node2]:
                parent[p_node2] = p_node1
            elif rank[p_node2] > rank[p_node1]:
                parent[p_node1] = p_node2
            
            else:
                parent[p_node2] = p_node1
                rank[p_node1] += 1
            
        
        row_len = len(grid)
        col_len = len(grid[0])
        
        #              down    right   up      left
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        accessible = [[2, 5, 6], [1, 3, 5], [2, 3, 4], [1, 4, 6]]
        able_to_move = [[2, 3, 4], [1, 4, 6], [2, 5, 6], [1, 3, 5]]

        rank = defaultdict(int)
        parent = defaultdict(tuple)
        
        for row in range(row_len):
            for col in range(col_len):
                parent[(row, col)] = (row, col)
        
        for row in range(row_len):
            for col in range(col_len):

                for index in range(4):
                    
                    nr = row + directions[index][0]
                    nc = col + directions[index][1]
                    
                    if valid_cell(nr, nc) and valid_path((row, col), (nr, nc), index):
                        union((row, col), (nr, nc))
        
        # start = find((0, 0))
        # end = find((row_len - 1, col_len - 1))
        # print(start, end)
        return find((0, 0)) == find((row_len - 1, col_len - 1))
                
        
        
        
        
        
        
        
        
        
        
        
        
        