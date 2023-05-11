class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def dfs(node):
            
            # cycle found
            if color[node] == 1:
                return False
            
            # mark as explored
            color[node] = 1
            
            cycle = False
            for child in graph[node]:
                if color[child] == 2:
                    continue
                    
                if not dfs(child):
                    cycle = True # cycle exists
            
            
            
            if cycle:
                return False
            else:
                output.append(node)
                color[node] = 2
                return True
        
        
        n = len(graph)
        color = [0] * n
        
        output = []
        for node in range(n):
            
            if color[node] != 0:
                continue
            else:
                dfs(node)
        
        output.sort()
        return output
