
# Link: https://leetcode.com/problems/range-sum-of-bst/
#Q: 938. Range Sum of BST

# Time: O(N)
# Space: O(H)

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def inorder(root, total):
            if not root: return total
            total = inorder(root.left, total)
            if low <= root.val <= high:
                total += root.val
            total = inorder(root.right, total)
            return total
        
        return inorder(root, 0)

# Time: O(N)
# Space: O(H)

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.out = 0
        def helper(root):
            if not root: return
            if low <= root.val <= high:
                self.out += root.val
            if root.val > low: helper(root.left)
            if root.val < high: helper(root.right)
        
        helper(root)
        return self.out
        
