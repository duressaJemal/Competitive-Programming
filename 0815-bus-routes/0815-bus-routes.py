class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        rout_map = defaultdict(set)
        if source == target:
            return 0
        
        for index, route in enumerate(routes):
            for station in route:
                rout_map[station].add(index)
        
        cur = []
        visited = set()

        for val in rout_map[source]:
            cur.append(val)
            visited.add(val)
        queue = deque(cur)    
        level = 1
        
        while queue:
            
            n = len(queue)
            for _ in range(n):
                
                index = queue.popleft()
                
                for station in routes[index]:
                    if station == target:
                        return level
                    
                    for bus_location in rout_map[station]:
                        if bus_location not in visited:
                            queue.append(bus_location)
                            visited.add(bus_location)
            level += 1
        
        return -1
                        
                