class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(row, n):
            visited.add(row)
            for col in range(n):
                if col not in visited and isConnected[row][col] == 1:
                    dfs(col, n)
                    
        n = len(isConnected)
        count = 0
        visited = set()
        
        for row in range(n):
            if row not in visited:
                count += 1
                dfs(row, n)
                
        return count
        