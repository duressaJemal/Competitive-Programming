# link: https://leetcode.com/problems/number-of-provinces/submissions/

# DFS

# Time: O(N^2)
# Space: O(N^2)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        

        n = len(isConnected)
        visited = set()
        province = 0
        
        def dfs(r):
            
            count = 0
            
            for c in range(n):
                
                if (r, c) in visited:
                    continue
                
                visited.add((r, c))
                
                if isConnected[r][c] == 1:
                    visited.add((c, r))
                    count += 1
                    dfs(c)
            
            return count
                
            
        
        for row in range(n):
            province += dfs(row)
            
        return province

        
