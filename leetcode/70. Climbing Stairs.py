class Solution:
    def climbStairs(self, n: int) -> int:
        
    # TOP DOWN
        d = {}
        def climb(index):
            
            if index <= 1:
                return 1
            
            if index in d:
                return d[index]
            steps = climb(index - 1) + climb(index - 2)
            if index not in d:
                d[index] = steps 
                
            return steps
        
        return climb(n)
        
    # BOTTOM UP
    
    def climbStairs(self, n: int) -> int:

        first, second = 1, 1
        
        for i in range(n - 1):
            temp = first
            first += second
            second = temp
            
        return first
