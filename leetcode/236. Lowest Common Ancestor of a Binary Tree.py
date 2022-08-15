
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        lca_node = None
        
        def dfs(node):
            
            nonlocal lca_node
            
            if not node or lca_node != None: return False
            left = dfs(node.left)
            right = dfs(node.right)
            
            current = node == p or node == q
            
            if (current and left) or (current and right) or (left and right):
                lca_node = node
                
            return current or left or right
        
        dfs(root)
        
        return lca_node
