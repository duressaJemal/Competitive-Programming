# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#Q: 235. Lowest Common Ancestor of a Binary Search Tree

# Time: O(H)
# Space: O(H)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

        small = min(p.val, q.val)
        large = max(p.val, q.val)
        
        while root:
            if root.val < small:
                root = root.right
            elif root.val > large:
                root = root.left
            else:
                return root
        
        
# Time: O(N)
# Space: O(H)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.output = 0
        def dfs(root):
            if not root: return None
            left = dfs(root.left)
            right = dfs(root.right)
            
            current = root.val == p.val or root.val == q.val
            
            if (current and left) or (current and right) or (left and right):
                self.output = root
                return True
            
            return current or left or right
        
        dfs(root)
        return self.output


























