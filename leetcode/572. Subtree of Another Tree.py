# Link: https://leetcode.com/problems/subtree-of-another-tree/
#Q: 572. Subtree of Another Tree

# Time: O(N*M)
# Space: O(N)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same_tree(root1, root2):

            if not root1 or not root2:
                if not root1 and not root2:
                    return True
                return False
            if root1.val != root2.val: return False
            return same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)
        
        
        def dfs(root, subRoot):
            if not root: return False
            return same_tree(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)
        return dfs(root, subRoot)
