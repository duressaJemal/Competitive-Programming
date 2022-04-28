class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        s = list(s)
        
        for string in s:
            if string == "]":
                container = []
                popped = stack.pop()
                
                while not popped.isnumeric() and stack:
                    container.append(popped)
                    popped = stack.pop()
                    
                container = container[:-1]
                container = container[::-1]
                lenght = int(popped)
                
                for i in range(lenght):
                    stack += container

            else:
                
                # for concatenating number strigs
                if stack and  stack[-1].isnumeric() and string.isnumeric():
                    stack[-1] = stack[-1] + string
                    continue
                    
                stack.append(string)
                
        return "".join(stack)
        
                    
