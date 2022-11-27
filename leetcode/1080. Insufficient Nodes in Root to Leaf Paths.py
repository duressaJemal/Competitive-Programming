# Link: https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        #Post order
        def insufficient_path(root, total):
            if not root: return 1
            total += root.val
            if not root.left and not root.right:
                if total < limit:
                    return 1
                return 0
            
            left = insufficient_path(root.left, total)
            right = insufficient_path(root.right, total)
            
            if left:
                root.left = None
            if right:
                root.right = None
                
            if left + right == 2:
                return 1
            return 0
        
        return None if insufficient_path(root, 0) else root

    
    
    
    
