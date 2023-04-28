class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def turn(node, index):
            cur = node
            cur_digit = int(cur[index])
            
            add = cur_digit + 1
            if add == 10:
                add = 0
            
            sub = cur_digit - 1
            if sub == -1:
                sub = 9
            
            return (cur[:index] + str(add) + cur[index + 1:], cur[:index] + str(sub) + cur[index + 1:])
            

        queue = deque(["0000"])
        visited = {"0000"}
        
        deadends = Counter(deadends)
        
        if queue[0] in deadends:
            return -1

        level = 0 
        while queue:

            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node == target:
                    return level
                
                for index in range(4):
                    add, sub = turn(node, index)
                    if add not in deadends and add not in visited:
                        queue.append(add)
                        visited.add(add)
                    
                    if sub not in deadends and sub not in visited:
                        queue.append(sub)
                        visited.add(sub)
            
            # update level
            level += 1
        
        return -1
                        
                    
                        
                    
                
                
                
                       
                     
                            
                      
                      
            
                     
                
                
                       
                       
                       
        
            

                    


                       
                       


            
        
        
        