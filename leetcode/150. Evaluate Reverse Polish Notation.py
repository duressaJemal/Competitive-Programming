# link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

# time: O(n)
# space: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ("+", "-", "/", "*")
        stack = []
        
        for token in tokens:
            
            if token not in operators:
                stack.append(token)
            else:
                right = stack.pop()
                left  = stack.pop()
                value = eval(left + token + right)
                if value > 0:
                    stack.append(str(floor(value)))
                else:
                    stack.append(str(ceil(value)))
            
        return int(stack[0])
        
        
