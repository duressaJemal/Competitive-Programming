# Time: O(V + E)
# Space: O(V + E)

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(node, arr):
            if node == len(graph) - 1:
                res.append(arr.copy())
                return
            
            for child in graph[node]:
                arr.append(child)
                dfs(child, arr)
                arr.pop()
                
            return
        
        res = []
        dfs(0, [0])
        return res