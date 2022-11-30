
# Link: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
#Q: 1026. Maximum Difference Between Node and Ancestor

# DFS(1)

# Time: O(N)
# Space: O(N)

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.diff = 0
        
        def dfs(root, mn, mx):
            if not root: return
            
            self.diff = max(self.diff, abs(mn - root.val), abs(mx - root.val))
            
            mn = min(mn, root.val)
            mx = max(mx, root.val)
            
            dfs(root.left, mn, mx)
            dfs(root.right, mn, mx)
            
        dfs(root, root.val, root.val)
        return self.diff
        
# DFS(2)

# Time: O(N)
# Space: O(N)

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        self.diff = 0
        def dfs(root):
            if not root: return (float("inf"), float("-inf")) # (max, min)
            if not root.left and not root.right: return (root.val, root.val)
    
            l_min, l_max = dfs(root.left)
            r_min, r_max = dfs(root.right)
            
            mn = min(l_min, r_min)
            mx = max(l_max, r_max)
            
            self.diff = max(self.diff, abs(mn - root.val), abs(mx - root.val))
            
            mn = min(mn, root.val)
            mx = max(mx, root.val)
            
            return (mn, mx)
        
        dfs(root)
        return self.diff
