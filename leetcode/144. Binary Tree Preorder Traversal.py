# Link: https://leetcode.com/problems/binary-tree-preorder-traversal/

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
