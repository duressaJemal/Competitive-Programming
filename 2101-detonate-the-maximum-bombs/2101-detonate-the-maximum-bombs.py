class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        # build graph
        graph = defaultdict(set)
        n = len(bombs)
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i != j:
                    x2, y2, r2 = bombs[j]
                    dis = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                    if dis <= r1:
                        graph[(x1, y1, i)].add((x2, y2, j))

        def dfs(node):
            
            visited.add(node)
            count = 1
            for child in graph[node]:
                if child not in visited:
                    count += dfs(child)
            return count
        
        res = 1
        for index in range(n):
            cur = bombs[index]
            node = (cur[0], cur[1], index)
            visited = set()
            res = max(res, dfs(node))
        
        return res
            
        
        
        
        
        
                    
                    