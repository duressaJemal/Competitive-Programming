
# Link: https://leetcode.com/problems/trim-a-binary-search-tree/
#Q: 669. Trim a Binary Search Tree

# Time: O(N)
# Space: O(H)

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def postorder(root):
            
            if not root: return None
            if low <= root.val <= high:
                root.left = postorder(root.left)
                root.right = postorder(root.right)
                return root
            else:
                if root.val < low:
                    return postorder(root.right)
                if root.val > high:
                    return postorder(root.left)
                
        return postorder(root)
        
