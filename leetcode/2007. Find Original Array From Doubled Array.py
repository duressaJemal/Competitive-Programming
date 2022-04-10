class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        
        if len(changed) % 2 != 0:
            
            return []
        
        dt = {}
        output = []
        changed.sort()
        
        for i in changed:
            
            if i in dt:
                dt[i] +=1
            else:
                dt[i] = 1
        print(dt)


        for k in dt:
        
            if dt[k] == 0:
                continue
            if k * 2 in dt and dt[k*2] != 0:
                if k == 0:
          
                    sub = dt[k]//2
                    dt[k] = dt[k] % 2
    
                    for i in range(sub):
                        output.append(k)
                    continue

                m = min(dt[k], dt[k*2])
                dt[k]-= m
                dt[k*2] -=m
       
                for i in range(m):
                    output.append(k)
         
        for key in dt:
            
            if dt[key] != 0:
                return []
        
        return output
