# Time: O(V + E)
# Space: O(V + E)

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(node, arr):
            
            if node == len(graph) - 1:
                arr.append(node)
                res.append(arr.copy())
                arr.pop()
                return
            
            visited.add(node)
            arr.append(node)
            
            for child in graph[node]:
                if child not in visited:
                    dfs(child, arr)
            
            arr.pop()
            visited.remove(node)
            return
        
        visited = set()
        res = []
        dfs(0, [])
        
        return res