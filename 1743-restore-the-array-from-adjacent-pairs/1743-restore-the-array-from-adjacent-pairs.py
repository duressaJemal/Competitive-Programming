class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        # build graph
        # start from node with one neighbour
        
        # then append while alternating and also keeping visited
        
        
        adj = defaultdict(list)
        
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)
        
        # find root
        root = None
        for key in adj:
            if len(adj[key]) == 1:
                root = key
                break
                
        
        def dfs(root):
            
            if root in visited:
                return 
            
            visited.add(root)
            output.append(root)
            
            for child in adj[root]:
                dfs(child)
         
        output = []
        visited = set()
        dfs(root)
        
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        