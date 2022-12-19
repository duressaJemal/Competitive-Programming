# Link: https://leetcode.com/problems/root-equals-sum-of-children/
#Q: 2236. Root Equals Sum of Children

# Time: O(1)
# Space: O(1)

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root.left and not root.right: return root.val
            return root.val == (dfs(root.left) + dfs(root.right))
        return dfs(root)
            
