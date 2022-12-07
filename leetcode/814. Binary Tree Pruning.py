# Link: https://leetcode.com/problems/binary-tree-pruning/
#Q: 814. Binary Tree Pruning

# Time: O(N)
# Space: O(H)

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if not root: return False
            left = dfs(root.left)
            right = dfs(root.right)
            
            if not left:
                root.left = None
            if not right:
                root.right = None
            
            current = root.val == 1
            return current or left or right
        
        return root if dfs(root) else None
