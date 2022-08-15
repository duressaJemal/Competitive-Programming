# Link: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# DFS -- Approach 1

# Time: O(N)
# Space: O(N)

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return (None, 0)
            
            left_ca, left_height = dfs(node.left)
            right_ca, right_height = dfs(node.right)
            
            if left_height == right_height:
                return (node, left_height + 1)
            elif left_height > right_height:
                return (left_ca, left_height + 1)
            else:
                return (right_ca, right_height + 1)
        
        return dfs(root)[0]

# DFS -- Approach 2

# Time: O(N^2)
# Sapce: O(N)

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return null
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        if left == right: return root
        if left > right: return self.lcaDeepestLeaves(root.left)
        else: return self.lcaDeepestLeaves(root.right)
        
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
        
        
            
            
        
        
        
        
        
        
        
        
