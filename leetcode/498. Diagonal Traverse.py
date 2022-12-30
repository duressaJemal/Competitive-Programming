# Link: https://leetcode.com/problems/diagonal-traverse/
#Q: 498. Diagonal Traverse

# Time: O(M*N)
# Space: O(1)

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n = len(mat[0])
        
        direction = "U"
        
        output = []
        i, j = 0, 0
        
        for diagonal in range(m + n - 1):
            
            if direction == "U":
                output.append(mat[i][j])
                while i - 1 >= 0 and j + 1 < n:
                    i -= 1
                    j += 1
                    output.append(mat[i][j])
                if j + 1 < n:
                    j += 1
                else:
                    i += 1
                direction = "D"
                
            else:
                output.append(mat[i][j])
                while i + 1 < m and j - 1 >= 0:
                    i += 1
                    j -= 1
                    output.append(mat[i][j])
                if i + 1 < m:
                    i += 1
                else:
                    j += 1
                direction = "U"
        
        return output
            
    
# From discuss section

"""

- Observation: cells on the same diagonal have equal sum of (i + j)
- create dictionary with keys of sum of (i + j)
- iterate over the grid and store all the digonal values based on the key of (i + j)
- iterate over dictonary key value and print the value based on diagonal parity ( odd diagonals and even diagaons) one must be reversed.
- return the accumelated value

"""
        
