# Link: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# DFS

# Time: O(N)
# Space: O(N))

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.output = 0
        
        def dfs(node, max_value, min_value):
            
            if not node: return
            
            self.output = max(self.output, abs(max_value - node.val), abs(min_value - node.val))
            
            max_value = max(max_value, node.val)
            min_value = min(min_value, node.val)
    
            dfs(node.left, max_value, min_value)
            dfs(node.right, max_value, min_value)
            
            
        dfs(root, root.val,root.val)
        
        return self.output
