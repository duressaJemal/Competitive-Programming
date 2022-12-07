# Link: https://leetcode.com/problems/longest-univalue-path/
#Q: 687. Longest Univalue Path

# Time: O(N)
# Space: O(H)

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node: return (None, 0)
            l_node, l_count = dfs(node.left)
            r_node, r_count = dfs(node.right)
            
            path_count = 1
            if node.val == l_node and node.val == r_node:
                self.count = max(self.count, l_count + r_count + 1)
                path_count = max(l_count, r_count) + 1 
            elif node.val == l_node:
                path_count = l_count + 1
            elif node.val == r_node:
                path_count = r_count + 1
            
            self.count = max(self.count, path_count)
            return (node.val, path_count)
        
        self.count = 1
        dfs(root)
        return self.count - 1
        
        
        
        
        
        
        
        
        
