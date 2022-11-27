
# Link: https://leetcode.com/problems/delete-leaves-with-a-given-value/
#Q: 1325. Delete Leaves With a Given Value

# Time: O(N)
# Space: O(H)

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        
        def helper(root):
            if not root: return 0

            left = helper(root.left)
            right = helper(root.right)

            if not left:
                root.left = None
            if not right:
                root.right = None

            if not root.left and not root.right and root.val == target:
                return 0
            else:
                return 1
    
        return root if helper(root) else None
