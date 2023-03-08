# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(N)
# Space: O(N)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(root):
        
            if not root:
                return None
            
            if val == root.val:
                return root
            
            if val > root.val:
                return dfs(root.right)
            else:
                return dfs(root.left)
        
        return dfs(root)
            