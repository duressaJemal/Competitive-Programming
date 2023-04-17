class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(root):
            if not root: return
            output.append(str(root.val))
            
            if not root.left and not root.right:
                return
            
            output.append("(")
            dfs(root.left)
            output.append(")")
            
            if root.right:
                output.append("(")
                dfs(root.right)
                output.append(")")
          
        output = []
        dfs(root)
        return "".join(output)