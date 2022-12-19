# Link: https://leetcode.com/problems/matrix-block-sum/
#Q: 1314. Matrix Block Sum

# Time: O(M*N*K)
# Space: O(M*N)

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m)]
        ans = [[0] * n for _ in range(m)]
        
        # build prefix sum
        for i in range(m):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i][j - 1] + mat[i][j - 1]
        
        for i in range(m):
            for j in range(n):
                
                # generate all the cordinates
                total = 0
                col_start, col_end = max(j - k, 0), min(j + k, n - 1)
                for row in range(max(i - k, 0), min(i + k, m - 1) + 1):
                    total += (prefix[row][col_end + 1] - prefix[row][col_start])
                
                ans[i][j] = total
        
        return ans
        
