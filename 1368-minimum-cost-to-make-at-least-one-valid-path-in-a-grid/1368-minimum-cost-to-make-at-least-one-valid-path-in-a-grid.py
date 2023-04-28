# class Solution:
#     def minCost(self, grid: List[List[int]]) -> int:
        
#         row_len = len(grid)
#         col_len = len(grid[0])
        
#         def is_valid(row, col):
#             if row < 0 or col < 0 or row >= row_len or col >= col_len:
#                 return False
#             else:
#                 return True
            
        
#         def explore(row, col, dircetion):
            
#             # base case
#             if not is_valid(row, col):
#                 return float("inf")
            
#             if (row, col) in visited:
#                 return visited[(row, col)]
            
#             marked.add((row, col))
            
#             cur = float("inf")
#             dir = [(1, 0, 4), (0, 1, 2), (-1, 0, 3), (0, -1, 1)]
            
#             for x, y in dir:
#                 nr = row + x
#                 nc = col + y
                
#                 if (nr, nc) not in marked:
#                     cur = min(cur, explore(nr, nc, grid[row][col]))
                    
#             visited((row, col)) = cur # memoize
#             marked.pop((row, col)) # remove from marked
            
            
                
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
            
        rowLen = len(grid[0])
        colLen = len(grid)
        
        
        def is_valid(row, col):
            if row < 0 or col < 0 or row >= colLen or col >= rowLen:
                return False
            else:
                return True
        
        heap = [(0,(colLen-1,rowLen-1))]
        best = collections.defaultdict(lambda :float('inf'))
        best[(colLen-1,rowLen-1)] = 0
        dirc = [(0, -1),(0, 1),   (-1, 0),(1, 0)]
        
        while heap:
            
            dist,loc = heapq.heappop(heap)
            x,y = loc
            if x == 0 and y == 0:
                return dist
            best[(x, y)] = min(best[(x, y)], dist)
            
            for i,d in enumerate(dirc):
                r,c = d
                if not is_valid(x+r,y+c):
                    continue
                r += x
                c += y
                currDir = grid[r][c]
                newDist = dist
                if currDir-1 != i:
                    newDist+=1
                if newDist < best[(r,c)]:
                    heapq.heappush(heap,(newDist,(r,c)))
                    
            