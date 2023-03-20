# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert(val, root):
            
            if not root:
                return TreeNode(val)
            
            if val < root.val:
                root.left = insert(val, root.left)
            elif val > root.val:
                root.right = insert(val, root.right)
            
            return root
            
        return insert(val, root)