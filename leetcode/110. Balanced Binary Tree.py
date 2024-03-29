# Link: https://leetcode.com/problems/balanced-binary-tree/
#Q: 110. Balanced Binary Tree

# Time: O(N)
# Space: O(H)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return dfs(root) != -1
