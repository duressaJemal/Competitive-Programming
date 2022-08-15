# Link: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return (None, 0)
            
            left_ca, left_height = dfs(node.left)
            right_ca, right_height = dfs(node.right)
            
            if left_height == right_height: return (node, left_height + 1)
            elif left_height > right_height: return (left_ca, left_height + 1)
            else: return (right_ca, right_height + 1)
            
        return dfs(root)[0]
        
