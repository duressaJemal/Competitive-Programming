# Time: O(N)
# Space: O(N)

class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        in_degree = [0 for _ in range(numCourses)]
        
        for end, start in pre:
            graph[start].append(end)
            in_degree[end] += 1
        
        queue = deque([])
        for node in range(numCourses):
            if not in_degree[node]:
                queue.append(node)
            
        order = []
        
        while queue:
            
            l = len(queue)
            for _ in range(l):
                
                node = queue.popleft()
                order.append(node)
                
                for child in graph[node]:
                    in_degree[child] -= 1
                    if not in_degree[child]:
                        queue.append(child)
        
        if len(order) == numCourses:
            return True
        else:
            return False
                
            