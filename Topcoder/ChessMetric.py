# Link: https://community.topcoder.com/stat?c=problem_statement&pm=1592&rd=4482

class ChessMetric:
    def howMany(self, size, start, end, numMoves):
        dirc = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1), (-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
        ways = [[0 for _ in range(size)] for _ in range(size)]

        ways[start[0]][start[1]] = 1


        for i in range(numMoves):
            temp = [[0 for _ in range(size)] for _ in range(size)]
            for x in range(size):
                 for y in range(size):
                    temp[x][y] = ways[x][y]
            for x in range(size):
                for y in range(size):
                    ways[x][y] = 0
                
            for x in range(size):
                for y in range(size):
                    for r, c in dirc:
                        nr = x + r
                        nc = y + c
                        
                        if nr < 0 or nr >= size or nc < 0 or nc >= size: continue
                        ways[nr][nc] += temp[x][y]

        return ways[end[0]][end[1]]



# 3
# {0,0}
# {1,0}
# 1
# Returns: 1
# Only 1 way to get to an adjacent square in 1 move


    	
# 100
# {0,0}
# {0,99}
# 50
# Returns: 243097320072600
