class Solution:
    def racecar(self, target: int) -> int:
        
        queue = deque([(0, 1)])
        visited = {(0, 1)}
        
        level = 0
        while queue:
            
            n = len(queue)
            for _ in range(n):
                
                position, speed = queue.popleft()
                if position == target:
                    return level
                
                # reverse
                rev = (position, -1 if speed > 0 else 1)
                if rev not in visited:
                    queue.append(rev)
                    visited.add(rev)
                
                # accelerate
                acc = (position + speed, speed * 2)
                if acc not in visited:
                    queue.append(acc)
                    visited.add(acc)
                
            # increment level
            level += 1
        
        
                
                
                
                