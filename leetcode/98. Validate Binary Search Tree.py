
# Link: https://leetcode.com/problems/validate-binary-search-tree/
#Q: 98. Validate Binary Search Tree

# Time: O(N)
# Space: O(H)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
    
        def dfs(root, mn, mx):
            if not root: return True
            if root.val <= mn or root.val >= mx: return False
            left = dfs(root.left, mn, min(mx, root.val))
            if not left:
                return False
            right = dfs(root.right, max(mn, root.val), mx)
            
            return left and right
        
        
        return dfs(root, float("-inf"), float("inf"))

# Time: O(N)
# Space: O(H)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.ans = True
        self.min = float("-inf")
        
        def helper(root):
            if not root: return
            helper(root.left)
            if root.val <= self.min:
                self.ans = False
            self.min = root.val
            helper(root.right)
        
        helper(root)
        return self.ans
        
        
