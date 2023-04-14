# Time: O(V + E)
# Space: O(V + E)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def bipartite(node, color):
            
            visited[node] = color 
            for child in graph[node]:
                if child in visited:
                    if visited[child] == color: return False
                else:
                    if not bipartite(child, 1 - color):
                        return False     
            return True
        
        n = len(graph)
        visited = {}
        
        for node in range(n):
            if node not in visited:
                if not bipartite(node, 1):
                    return False
        
        return True
                
                    