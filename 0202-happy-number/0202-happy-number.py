class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        
        while n not in visited:
            visited.add(n)
            n = sum(int(x) ** 2 for x in str(n))
        
        return n == 1
        
        