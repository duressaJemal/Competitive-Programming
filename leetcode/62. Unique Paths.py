# link https://leetcode.com/problems/unique-paths/

# space O(m + n)
# time O( m * n ) 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        
        def helper(r, c):
            
            if (r, c) in memo: return memo[(r,c)]
            if r == m or c == n: return 0
            if r == m - 1 and c == n - 1: return 1
            
            memo[(r, c)] = helper(r + 1, c) + helper(r, c + 1)
           
            return memo[(r, c)]
        
        return helper(0, 0)
        
