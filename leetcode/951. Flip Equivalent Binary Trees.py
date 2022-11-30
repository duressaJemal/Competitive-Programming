
# Link: https://leetcode.com/problems/flip-equivalent-binary-trees/
#Q: 951. Flip Equivalent Binary Trees

# Time: O(N+M) , where N = len(root1) and M = len(root2)
# Space: O(N+M)

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:        
            def dfs(root1, root2):
                if not root1 or not root2:
                    if not root1 and not root2:
                        return True
                    return False

                if root1.val == root2.val:
                    return (dfs(root1.left, root2.left) and dfs(root1.right, root2.right)) or(dfs(root1.left, root2.right) and dfs(root1.right, root2.left))
                return False
            return dfs(root1, root2)
            
            
            
            
            
            
            
            
            
