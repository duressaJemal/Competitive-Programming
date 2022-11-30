

# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#Q: 236. Lowest Common Ancestor of a Binary Tree

# Time: O(N)
# Space: O(N)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.output = root
        def dfs(root):
            
            if not root: return root
            left = dfs(root.left)
            right = dfs(root.right)
        
            current = root.val == p.val or root.val == q.val
            
            if (current and left) or (current and right) or (left and right):
                self.output = root
                return True
            return current or left or right

        dfs(root)
        return self.output
