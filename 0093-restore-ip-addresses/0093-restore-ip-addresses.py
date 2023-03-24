class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        count = [0]
        output = []
        
        def backtrack(arr, index):
            
            if index == len(s):

                if len(arr) == 4:
                    output.append(".".join(arr))
                return
            
            for step in range(0, len(s) - index):
                
                cur = s[index : index + step + 1]
                
                if int(cur) > 255 or (cur[0] == "0" and len(cur) > 1):
                    return
    
                # add
                arr.append(cur)
                backtrack(arr, index + step + 1)
                # remove
                arr.pop()

            
        backtrack([], 0)
        return output
            
                

                
                
                    
            
            
            
            
            
            
                    