class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        """
        count the degree for each node
        take the maximum ones
        
        from the maximums check if there exist a pair that is not connected.
            if:
                return max + max
            else:
                return max + max - 1
        
        """
        
        counter = defaultdict(int)
        edge_list = set()
        
        for road in roads:
            counter[road[0]] += 1
            counter[road[1]] += 1
            edge_list.add((road[0], road[1]))
        
        pairs = []
        for key in counter:
            pairs.append(key)
            
        mx = 0
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                if (pairs[i], pairs[j]) not in edge_list and (pairs[j], pairs[i]) not in edge_list:
                    mx = max(mx, counter[pairs[i]] + counter[pairs[j]])
                else:
                    mx = max(mx, (counter[pairs[i]] + counter[pairs[j]]) - 1)
            
        return mx
        
        
            
        
        