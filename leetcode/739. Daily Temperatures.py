from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures):
        
        output = [0] * len(temperatures)
        stack = deque([])

        for index, value in enumerate(temperatures):

            while stack and value > stack[-1][1]:
                output[stack[-1][0]] = index - stack[-1][0]
                stack.pop()

            stack.append((index, value))

        return output
