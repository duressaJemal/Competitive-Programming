class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        n = len(quiet)
        
        graph = defaultdict(list)
        hash_map = defaultdict(int)
        in_degree = [0] * n
        
        # create quietness map
        for index, val in enumerate(quiet):
            hash_map[val] = index
        
        for start, end in richer:
            graph[start].append(end)
            in_degree[end] += 1
        
        # queue initialization
        queue = deque([])
        for node in range(n):
            if not in_degree[node]:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                
                # update quietness
                quiet[child] = min(quiet[child], quiet[node])
                in_degree[child] -= 1
                
                if not in_degree[child]:
                    queue.append(child)
        
        output = []
        for val in quiet:
            output.append(hash_map[val])
        
        return output
                
    
                    
                
            
        
        