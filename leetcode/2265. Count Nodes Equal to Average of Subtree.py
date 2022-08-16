# Link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        self.count = 0
        
        def dfs(node):
            
            if not node: return (0, 0) # (sum, count)
            
            left_sum, left_nodes = dfs(node.left)
            right_sum, right_nodes = dfs(node.right)
            
            total = left_sum + right_sum + node.val
            subtree_nodes = left_nodes + right_nodes + 1
            
            if total // subtree_nodes == node.val:
                self.count += 1
            
            return (total, subtree_nodes)
        
        
        dfs(root)
        return self.count
