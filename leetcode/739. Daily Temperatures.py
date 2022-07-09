# link: https://leetcode.com/problems/daily-temperatures/submissions/

# time: O(n)
# space: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        output = [0] * n
        stack = []
        
        for index, value in enumerate(temperatures):
            while stack and temperatures[index] > stack[-1][1]:
                popped_item = stack.pop()
                output[popped_item[0]] = index - popped_item[0]
            stack.append((index, temperatures[index]))
            
        return output
        
        
