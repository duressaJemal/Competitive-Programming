class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def backtrack(cur, index):
        
            if index == len(arr):
                if len(visited) == len(cur):
                    max_length[0] = max(max_length[0], len(cur))
                return
        
            value = arr[index]
            is_valid = True
            
            for char in value:
                if char in visited:
                    is_valid = False
                    break
                    
            if is_valid:
                for char in value:
                    visited.add(char)
                backtrack(cur + value, index + 1)
                for char in value:
                    if char in visited:
                        visited.remove(char)
                    
            backtrack(cur, index + 1)
            return
        
        max_length = [0]
        visited = set()
        backtrack("", 0)
        return max_length[0]
                
                
                
                
                
            
        