# Link: https://leetcode.com/problems/jump-game-iii/

# BFS

# Time: O(N)
# Space: O(N)

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)
        queue = deque([start])
        visited = set()
        
        while queue:
            
            parent = queue.popleft()
            if arr[parent] == 0: return True
            visited.add(parent)
            
            left = parent - arr[parent]
            right = parent + arr[parent]
            
            if left >= 0 and left not in visited: queue.append(left)
            if right < n and right not in visited: queue.append(right)
        
        return False
        
# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)
        visited = set()
        self.output = False
        
        def dfs(index):
            if index < 0 or index >= n: return
            if index not in visited:
                
                if arr[index] == 0: self.output = True
                visited.add(index)
                if not self.output:
                    dfs(index + arr[index])
                    dfs(index - arr[index])

        dfs(start)
        return self.output
        
        
        
        
