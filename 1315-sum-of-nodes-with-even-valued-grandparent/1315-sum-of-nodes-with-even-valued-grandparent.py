# Time: O(N)
# Space: O(H)

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def dfs(node, parent, grand_parent):
            if not node:
                return 0
            
            left = dfs(node.left, node.val, parent)
            right = dfs(node.right, node.val, parent)
            
            return left + right + (node.val if grand_parent % 2 == 0 else 0)
        
        return dfs(root, 1, 1)
            