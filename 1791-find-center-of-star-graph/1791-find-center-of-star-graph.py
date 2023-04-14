# Time: O(N)
# Space: O(N)

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        counter = defaultdict(int)
        
        for edge in edges:
            counter[edge[0]] += 1
            counter[edge[1]] += 1
        
        mx = (0, 0)
        
        for key in counter:
            mx = max(mx, (counter[key], key))
        
        return mx[1]
          
# FUN
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]
        
        
        
        
        
        