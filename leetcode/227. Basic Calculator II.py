# link: https://leetcode.com/problems/basic-calculator-ii/submissions/

# time: O(n)
# space: O(n)

class Solution:
    def calculate(self, s: str) -> int:
        
        n = len(s)
        operator, number = "+", 0
        stack = []
        
        for i in range(n):
            char = s[i]
            if char.isdigit():
                number = number * 10 + int(char)
            
            if (not char.isdigit() and not char.isspace()) or i == n - 1:
                
                if operator == "+":
                    stack.append(number)
                elif operator == "-":
                    stack.append(-number)
                elif operator == "*":
                    stack.append(stack.pop() * number)
                elif operator == "/":
                    popped = stack.pop()
                    if popped < 0:
                        stack.append(-((0 - popped) // number))
                    else:
                        stack.append(popped // number)
                operator = char
                number = 0
        
        end, output = 0, 0
        while end < len(stack):
            output += stack.pop()
        
        return output
            
            
# CHECK THE OPTIMIZED SOLUTION
            
