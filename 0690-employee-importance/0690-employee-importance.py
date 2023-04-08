"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        def dfs(node):
            count = node.importance
            for sub in node.subordinates:
                count += dfs(hash_map[sub])
            return count
        
        # map employee with their id
        n = len(employees)
        hash_map = {}
        for index in range(n):
            hash_map[employees[index].id] = employees[index]
        
        return dfs(hash_map[id])
    
    
            
            
            
            
            
            
            
            
            
            
            
            
        
        
            