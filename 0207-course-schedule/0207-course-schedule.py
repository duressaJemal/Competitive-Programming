# Time: O(N)
# Space: O(N)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build graph
        graph = defaultdict(list)
        for end, start in prerequisites:
            graph[start].append(end)
                
        def cycle_detection(node):
            color[node] = 1 # make it gray
            for child in graph[node]:
                if color[child] == 1:
                    return False
                if color[child] == -1: # if traversed before
                    continue
                else:
                    if not cycle_detection(child):
                        return False         
            color[node] = -1 # make it black
            return True
         
        color = [0] * numCourses
        for node in range(numCourses):
            if not color[node]:
                if not cycle_detection(node):
                    return False
        return True
    