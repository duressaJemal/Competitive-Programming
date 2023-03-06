class Solution:
    def decodeString(self, s: str) -> str:
        
        def extract_num(index):
            
            curr = ""
            while index < len(s) and s[index].isnumeric():
                curr += s[index]
                index += 1
            
            return (int(curr), index)
        
        def solve(num, index):
            
            string = ""
            
            while index < len(s) and s[index] != "]":
                if s[index].isnumeric():
                    next_num, index = extract_num(index)
                    ret = solve(next_num, index + 1) # starts from char
                    string += ret[0]
                    index = ret[1]
                else:
                    string += s[index]
                
                index += 1
                
            return (num * string, index)
        
        return solve(1, 0)[0]
        
        
                
            
                
                
                    
                
                

        
            