"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# link: https://leetcode.com/problems/employee-importance/submissions/

# DFS

# Time: O(N)
# Space: O(N)


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        dic = {employee.id: employee for employee in employees}   
        
        def dfs(id):
            
            employee = dic[id]
            return (employee.importance + sum(dfs(child) for child in employee.subordinates))
            
        return dfs(id)
            


# BFS

# Time: O(N)
# Space: O(N)


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emp = {e.id : e for e in employees}
        queue, total_importance = deque([emp[id]]), 0
        
        
        while queue:
            
            node = queue.popleft()
            total_importance += node.importance
            
            for child in node.subordinates:
                queue.append(emp[child])
            
        return total_importance
        
        
        
