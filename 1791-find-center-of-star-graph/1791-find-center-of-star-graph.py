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
            