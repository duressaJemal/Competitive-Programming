# Time: O(N)
# Space: O(1)

class Solution:
    def tribonacci(self, n: int) -> int:
        
        first = 0
        second = 1
        third  = 1
        
        for t in range(3, n + 1):
            cur = first + second + third
            first, second, third = second, third, cur
        
        return third if n else first