
# Link: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
#Q: 783. Minimum Distance Between BST Nodes

# Time: O(N)
# Space: O(H)

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        self.min = float("inf")
        
        def dfs(root, prev):
            if not root: return prev
            prev = dfs(root.left, prev)
            self.min = min(self.min, abs(root.val - prev))
            return dfs(root.right, root.val)
        
        dfs(root, float("-inf"))
        return self.min
