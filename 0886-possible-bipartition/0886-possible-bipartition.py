# Time: O(V + E) where V = vertex and E = edge
# Space: O(V + E)

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        # build graph
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
          
        def bipartite(node, color):
            
            visited[node] = color
            for child in graph[node]:
                if child in visited:
                    if visited[child] == color: return False
                else:
                    # early exit
                    if not bipartite(child, 1 - color):
                        return False
            return True
        
        visited = {}
        for node in graph:
            if node not in visited:
                if not bipartite(node, 1):
                    return False

        return True
        
                    