# Link: https://leetcode.com/problems/construct-string-from-binary-tree/
#Q: 606. Construct String from Binary Tree

# Time: O(N)
# Space: O(N)

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
            
# Time: O(N^2)
# Space: O(H)

# class Solution:
#     def tree2str(self, root: Optional[TreeNode]) -> str:
        
#         def dfs(root):
#             if not root: return ""
#             left = dfs(root.left)
#             right = dfs(root.right)
            
#             current = str(root.val)
            
#             if right:
#                 return current + "(" + left + ")" + "(" + right + ")"
#             if left:
#                 return current + "(" + left + ")"
#             return current
            
        
#         return dfs(root)
        
