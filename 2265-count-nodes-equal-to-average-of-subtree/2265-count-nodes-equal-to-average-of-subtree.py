# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(N)
# Space: O(N)

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        count = [0]
        
        def dfs(root):
            if not root: return (0, 0)
            
            l_t, l_c = dfs(root.left)
            r_t, r_c = dfs(root.right)
            
            total = l_t + r_t + root.val
            total_c = l_c + r_c + 1
            
            if root.val == total // total_c:
                count[0] += 1
                
            return (total, total_c)
        
        dfs(root)
        return count[0]