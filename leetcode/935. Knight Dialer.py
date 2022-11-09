# Link: https://leetcode.com/problems/knight-dialer/
#Q: 935. Knight Dialer

# Top-down

# Time: O(9*N) = O(N)
# Space: O(9*N)

class Solution:
    def knightDialer(self, n: int) -> int:
        
        memo = {}
        jumps = {1 : [6, 8], 2 : [7, 9], 3 : [4, 8], 4 : [0, 3, 9], 5 : [], 6 : [0, 1, 7], 7 : [2, 6], 8 : [1, 3], 9 : [2, 4], 0 : [4, 6]}
        
        def helper(i, j):
            if j == 0: return 1
            if (i, j) in memo: return memo[(i, j)]
            res = 0
            for x in jumps[i]:
                res += helper(x, j - 1)
            memo[(i, j)] = res
            return memo[(i, j)]
                
        output = 0
        for i in range(10):
            output += helper(i, n - 1)
        
        return output % (10**9 + 7)
      
# Bottom-up

# Time: O(9*N)
# Space: O(9*N)

class Solution:
    def knightDialer(self, n: int) -> int:
        
        dp = [[0] * (10) for _ in range(n + 1)]
        jumps = {1 : [6, 8], 2 : [7, 9], 3 : [4, 8], 4 : [0, 3, 9], 5 : [], 6 : [0, 1, 7], 7 : [2, 6], 8 : [1, 3], 9 : [2, 4], 0 : [4, 6]}
        
        for i in range(1, n + 1):
            for j in range(0, 10):
                if i == 1: 
                    dp[i][j] = 1
                else:
                    for x in jumps[j]:
                        dp[i][j] += dp[i - 1][x]
        
        res = 0
        for i in range(10):
            res += dp[n][i]
        
        return res % (10**9 + 7)

