
# Link: https://leetcode.com/problems/convert-bst-to-greater-tree/
#Q: 538. Convert BST to Greater Tree

# Time: O(N)
# Space: O(H)

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def reversed_inorder(root, total):
            if not root: return total
            root.val += reversed_inorder(root.right, total)
            total = reversed_inorder(root.left, root.val)
            return total
        
        reversed_inorder(root, 0)
        return root
        
# Using global variable

# Time: O(N)
# Space: O(H)

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        def reversed_inorder(root):
            if not root: return
            reversed_inorder(root.right)
            self.total += root.val
            root.val = self.total
            reversed_inorder(root.left)
        reversed_inorder(root)
        return root
            
            
            
