# Bottom-up

# Time: O(N)
# Space: O(1)

class Solution:
    def fib(self, n: int) -> int:
        left = 0
        right = 1
        
        for i in range(2, n + 1):
            temp = right
            left = right + left
            right, left = left, temp
        
        return 0 if not n else right
    
