class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            
            if not root: return float("-inf")
            if not root.left and not root.right: 
                result[0] = max(result[0], root.val)
                return max(root.val, 0)
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # possible update
            result[0] = max(result[0], left + right + root.val)
            
            # choose max of left and right
            choosen = max(left, right)
            if choosen <= 0:
                result[0] = max(result[0], root.val)
                return max(root.val, 0)
            else:
                result[0] = max(result[0], choosen + root.val)
                return choosen + root.val
            
            
    
        result = [float("-inf")]
        dfs(root)
        
        return result[0]
            