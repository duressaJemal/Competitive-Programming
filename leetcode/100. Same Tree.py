# Link: https://leetcode.com/problems/same-tree/

# DFS

# Time: O(p + q)
# Space: O(max(p, q))

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not(p and q):
            return p == q
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    
