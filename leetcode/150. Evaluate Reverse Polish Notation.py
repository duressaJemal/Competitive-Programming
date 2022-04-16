import math

class Solution:
    def evalRPN(self, tokens):

        operators = {"*", "+", "-", "/"}
        container = []
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                container.append(tokens[i])
            else:
                a = container.pop()
                b = container.pop()

                value = eval(b + tokens[i] + a)
                if value > 0:
                    container.append(str(math.floor(value)))
                else:
                    container.append(str(math.ceil(value)))
                    
        return int(container[0])
