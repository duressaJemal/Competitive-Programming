"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def dfs(root):
            
            cur_node = Node(root.val, [])
            visited[root] = cur_node
            
            temp = []
            for neigh in root.neighbors:
                if neigh not in visited:
                    cur  = dfs(neigh)
                    temp.append(cur)
                else:
                    temp.append(visited[neigh])
                
            cur_node.neighbors = temp
            return cur_node
            
        visited = {}
        
        if not node:
            return None
        
        return dfs(node)

            
        
            
            
            
                