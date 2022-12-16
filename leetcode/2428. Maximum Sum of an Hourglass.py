# Link: https://leetcode.com/problems/maximum-sum-of-an-hourglass/
#Q: 2428. Maximum Sum of an Hourglass

# Time: O(M*N)
# Space: O(1)

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        mx = 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if j + 2 < n and i + 2 < m:
                    total = 0
                    for c in range(j, j + 3):
                        total += grid[i][c]
                    for c in range(j, j + 3):
                        total += grid[i + 2][c]
                    total += grid[i + 1][j + 1]
                    mx = max(mx, total)
        return mx


