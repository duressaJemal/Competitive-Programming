# Link: https://leetcode.com/problems/transpose-matrix/
#Q: 867. Transpose Matrix

# Time: O(M*N)
# Space: O(M*N)

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m, n = len(matrix), len(matrix[0])
        output = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                output[i][j] = matrix[j][i]
        
        return output
