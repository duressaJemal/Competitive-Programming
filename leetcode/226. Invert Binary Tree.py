# Link: https://leetcode.com/problems/invert-binary-tree/
#Q: 226. Invert Binary Tree

# Time: O(N)
# Space: O(H)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(root):
            if not root: return None
            left = invert(root.left)
            right = invert(root.right)
            
            root.left = right
            root.right = left
            
            return root
        
        return invert(root)
