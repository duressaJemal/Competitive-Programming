class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []
        
        def backtrack(arr, visited):
            
            if len(arr) == n:
                res.append(arr.copy())
                return
            
            for value in nums:
                if value not in visited:
                    
                    # add
                    arr.append(value)
                    visited.add(value)
                    
                    backtrack(arr, visited)
                    
                    # remove
                    arr.pop()
                    visited.remove(value)
                    
        backtrack([], set())
        return res
            
            
                    
                    
            
                
            