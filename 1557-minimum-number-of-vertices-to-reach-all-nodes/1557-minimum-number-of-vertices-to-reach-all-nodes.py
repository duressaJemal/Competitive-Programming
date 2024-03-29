# Time: O(N)
# Space: O(N)

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        start = set()
        end = set()
        
        for edge in edges:
            start.add(edge[0])
            end.add(edge[1])
        
        return list(start - end)
            