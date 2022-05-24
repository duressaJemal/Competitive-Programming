#link https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

# time: O(n)
# space: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        

        if not root: return 0
        
        def dfs(root):
            if root.children == None: return 1
            
            depth = 0
            
            for children in root.children:
                depth = max(depth, dfs(children))
                
            return depth + 1

        return dfs(root)
    
