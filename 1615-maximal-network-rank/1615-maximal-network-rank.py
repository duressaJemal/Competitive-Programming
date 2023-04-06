# Time: O(N*2)
# Space: O(N)

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        counter = defaultdict(int)
        edge_list = set()
        
        for road in roads:
            counter[road[0]] += 1
            counter[road[1]] += 1
            edge_list.add(tuple(road))
        
        pairs = list(counter.keys())
            
        mx = 0
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                start = pairs[i]
                end = pairs[j]
                
                if (start, end) not in edge_list and (end, start) not in edge_list:
                    mx = max(mx, counter[start] + counter[end])
                else:
                    mx = max(mx, (counter[start] + counter[end]) - 1)
            
        return mx
        
        
            
        
        