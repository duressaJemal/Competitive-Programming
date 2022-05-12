class Solution:
    def calculate(self, s: str) -> int:
        
        s = s.replace (" ", "")
        s = list(s)
        
        # for concatinating numbers that are larger than 9
        start = 0
        while start < len(s):
            
            while start + 1 != len(s) and s[start].isnumeric() and s[start + 1].isnumeric():
                s[start] = s[start] + s[start + 1]
                s.pop(start + 1)
                
            start += 1
            
        if len(s) == 1: # early handling
            return int(s[0])
        
        higher = {"*", "/"}
        
        mult_div = []
        store = []
        
        # multiplication and division
        for string in s:
            if string in higher:
                store.append(string)
                
            else:
                
                if store and mult_div:
                    left = int(mult_div.pop())
                    
                    if store[-1] == "*":
                        mult_div.append(floor(left * int(string)))
                    else:
                        mult_div.append(floor(left / int(string)))
                    store.pop()
                    
                else:
                    mult_div.append(string)

        # addition
        add_sub = []
        lower = {"-", "+"}
        for value in mult_div:
            if value in lower:
                store.append(value)
            else: 
                if store and add_sub:
                    left = int(add_sub.pop())

                    if store[-1] == "+":
                        add_sub.append(left + int(value))
                    else:
                        add_sub.append(left - int(value))
                    store.pop()

                else:
                    add_sub.append(value)

            
        return int(add_sub[0])
            
            
            
