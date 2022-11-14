# Link: https://leetcode.com/problems/out-of-boundary-paths/
#Q: 576. Out of Boundary Paths

# Top-down

# Time: O(maxMoves*N*M)
# Space: O(maxMoves*N*M)

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        memo = {}
        def helper(moves, i, j):
            if i < 0 or j < 0 or i == m or j == n: return 1
            if moves == 0: return 0
            
            if (moves, i, j) in memo: return memo[(moves, i, j)]
            
            dirc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            res = 0
            
            for x, y in dirc:
                res += helper(moves - 1, i - x, j - y)
            
            memo[(moves, i, j)] = res
            return memo[(moves, i, j)]
        
        return helper(maxMove, startRow, startColumn)
            

# Bottom-up

# Time: O(maxMoves*M*N)
# Space: O(maxMoves*M*N)

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        dp = [[[0] * (n + 2) for _ in range(m + 2)] for _ in range(maxMove + 1)]
        
        for i in range(maxMove + 1):
            for j in [0, m + 1]:
                for k in range(n + 2):
                    dp[i][j][k] = 1
            
            for j in range(1, m + 2):
                for k in [0, n + 1]:
                    dp[i][j][k] = 1
        
        
        dirc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(1, maxMove + 1):
            for j in range(1, m + 1):
                for k in range(1, n + 1):
                    for x, y in dirc: 
                        dp[i][j][k] += dp[i - 1][j + x][k + y]
        
        return dp[maxMove][startRow + 1][startColumn + 1] % (10**9 + 7)





