# Link: https://leetcode.com/problems/evaluate-boolean-binary-tree/
#Q: 2331. Evaluate Boolean Binary Tree

# Time: O(N)
# Space: O(H)

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root.left and not root.right:
                return root.val
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            return (left or right) if root.val == 2 else (left and right)
        return dfs(root)
