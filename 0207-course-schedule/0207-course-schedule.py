class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        for end, start in prerequisites:
            graph[start].append(end)
                
        def cycle_detection(node):
            visited.add(node)
            traversed.add(node)
            
            for child in graph[node]:
       
                if child in visited:
                    return False
                
                if child in traversed:
                    continue
                else:
                    if not cycle_detection(child):
                        return False         
            visited.remove(node)
            return True
         
        visited = set()
        traversed = set()
        for node in range(numCourses -1, 0, -1):
            if node not in traversed:
                if not cycle_detection(node):
                    return False
        return True
    