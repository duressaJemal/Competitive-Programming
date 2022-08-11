# Link: https://leetcode.com/problems/univalued-binary-tree/

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, value):
            
            if not node: return True
            if node.val != value: return False
            return dfs(node.left, value) and dfs(node.right, value)
        
        return dfs(root, root.val)
        
