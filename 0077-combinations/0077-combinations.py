class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        res= []
        
        def backtrack(arr, start):
            
            if len(arr) == k:
                res.append(arr.copy())
                return 
            
            for value in range(start + 1, n + 1):
                arr.append(value)
                backtrack(arr, value)
                arr.pop()
            
        backtrack([], 0)
        return res