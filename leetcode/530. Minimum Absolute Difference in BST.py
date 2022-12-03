
# Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
#Q: 530. Minimum Absolute Difference in BST

# Time: O(N)
# Space: O(H)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.min = float("inf")
        def dfs(root, prev):
            if not root: return prev
            prev = dfs(root.left, prev)
            self.min = min(self.min, abs(root.val - prev))
            prev = dfs(root.right, root.val)
            return prev
        
        dfs(root, float("-inf"))
        return self.min
        
        
