# Time: O(N)
# Space: O(N)

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, total):
            # base case
            if not root:
                return
            # if leaf node
            total = total * 10 + root.val
            if not root.left and not root.right:
                result[0] += total
                return
            # recurence relation
            dfs(root.left, total)
            dfs(root.right, total)
            
            return
        
        result = [0]
        dfs(root, 0)
        return result[0]
        
        