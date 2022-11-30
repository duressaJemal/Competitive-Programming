# Link: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
#Q: 1123. Lowest Common Ancestor of Deepest Leaves

# Time: O(N)
# Space: O(H)

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root, depth):
            if not root: return (depth, None)
            left = dfs(root.left, depth + 1)
            right = dfs(root.right, depth + 1)
            
            if left[0] == right[0]:
                return (left[0], root)
            elif left[0] > right[0]:
                return left
            else:
                return right
            
        return dfs(root, 0)[1]
        


        
            
            
        
        
        
        
        
        
        
        
