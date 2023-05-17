# Time: O(N^2)

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        
        ancestor = [set() for _ in range(numCourses)]
        graph = defaultdict(list)
        in_degree = [0] * (numCourses + 1)
        output = []
        
        for start, end in prerequisites:
            graph[start].append(end)
            in_degree[end] += 1
            
        queue = deque([])
        for node in graph:
            if not in_degree[node]:
                queue.append(node)
        
        
        while queue:
            
            l = len(queue)
            for _ in range(l):
                
                node = queue.popleft()
                for child in graph[node]:
                    
                    in_degree[child] -= 1
                    if not in_degree[child]:
                        queue.append(child)
                        
                    for anc in ancestor[node]:
                        ancestor[child].add(anc)
                    ancestor[child].add(node)
                    

        # process each query
        for start, end in queries:
            
            if start in ancestor[end]:
                output.append(True)
            else:
                output.append(False)

        return output
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                