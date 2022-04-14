class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        openingTag = {"(":")", "{":"}", "[":"]"}
        closingTag = {")":"(", "}":"{", "]":"["}
        
        for i in range(len(s)): 
            if s[i] in openingTag:
                stack.append(s[i])
                continue
            if len(stack) > 0 and closingTag[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False
