class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        if not rooms:
            return True
        
        queue = deque([0] if rooms else [])
        visited = {0}
        
        while queue:
            node = queue.pop()
            
            for child in rooms[node]:
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
                
        
        for node in range(1, len(rooms)):
            if node not in visited:
                return False
        
        return True
    
            
            
            
            
            