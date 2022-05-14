#link https://leetcode.com/problems/solving-questions-with-brainpower/
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        d = {}
  
        def helper(index):
            if index >= len(questions):
                return 0

            if index in d:
                return d[index]
            
            maximum = 0
            solve = questions[index][0] + helper(index + questions[index][1] + 1) # if decided to solve
            skip = helper(index + 1) # if decided to skip
            maximum = max(solve, skip)
            
            if index not in d:
                d[index] = maximum
                
            return maximum
        
        return helper(0)
