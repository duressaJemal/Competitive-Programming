# Link: https://leetcode.com/problems/path-sum-iii/
#Q: 437. Path Sum III

# Time: O(N*2)
# Space: O(N)


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        output = 0
        def valid_path_sum(root, total):
            if not root: return 0
            total += root.val
            if total == targetSum:
                return 1 + valid_path_sum(root.left, total) + valid_path_sum(root.right, total)
            else:
                return valid_path_sum(root.left, total) + valid_path_sum(root.right, total)
        
        
        def preorder_traversal(root):
            nonlocal output
            if not root: return
            
            output += valid_path_sum(root, 0)
            preorder_traversal(root.left)
            preorder_traversal(root.right)
        
        preorder_traversal(root)
        return output
            
            
            
