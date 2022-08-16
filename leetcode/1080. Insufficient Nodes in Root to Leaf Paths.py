# Link: https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        def dfs(node, total):
            
            if not node: return True
            
            total += node.val

            if not node.left and not node.right:
                return total < limit
            
            left = dfs(node.left, total)
            right = dfs(node.right, total)
            
            
            if left and right:
                node.left = None
                node.right = None
                return True
            else:
                if left:
                    node.left = None
                if right:
                    node.right = None
                return False
        
        return None if dfs(root, 0) else root


    
    
    
    
