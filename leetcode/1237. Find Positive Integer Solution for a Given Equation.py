# Link: https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

# Binary search

# Time: (N * log(N)) -- where N = 1000
# Space: O(1)

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        output = []
        for x in range(1, 1000 + 1):
            
            left = 0 # first bad value
            right = 1000 # assume first good value
            
            while right > left + 1:
                mid = (left + right) // 2

                if customfunction.f(x, mid) >= z:
                    right = mid
                else:
                    left = mid
            
            if customfunction.f(x, right) == z:
                output.append([x, right])
        
        return output
                
                
