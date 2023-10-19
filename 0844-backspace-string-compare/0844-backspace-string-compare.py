class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def opp(arr, output):
            
            count = 0
            
            for i in range(len(arr) - 1, -1, -1):
                if arr[i] == "#":
                    count += 1
                    
                if not count:
                    output.append(arr[i])
                
                elif arr[i] != "#":
                    count -= 1
                    
                
            return output
                    
        output_s = opp(s, [])
        output_t = opp(t, [])
        
        print(output_s, output_t)
        
        return output_s == output_t
            