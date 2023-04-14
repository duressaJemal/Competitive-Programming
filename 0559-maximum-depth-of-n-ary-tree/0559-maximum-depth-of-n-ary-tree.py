"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(node):
            if not node: return 0
            cur = 0
            
            for child in node.children:
                cur = max(cur, dfs(child))
            
            return cur + 1
        
        return dfs(root)