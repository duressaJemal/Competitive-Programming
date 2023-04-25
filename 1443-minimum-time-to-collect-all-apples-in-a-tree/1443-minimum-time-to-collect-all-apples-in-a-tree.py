class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        
        def dfs(node):
            
            cur = 0
            visited.add(node)
            
            for child in graph[node]:
                if child not in visited:
                    cur += dfs(child)

            if cur or hasApple[node]:
                if node == 0: return cur
                return cur + 2
            else:
                return 0
        
        visited = set()
        return dfs(0)
                