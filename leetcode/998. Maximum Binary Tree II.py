# Link: https://leetcode.com/problems/maximum-binary-tree-ii/
#Q: 998. Maximum Binary Tree II

# Time: O(H)
# Space: O(H)

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(root):
            if not root: return TreeNode(val)
            
            if val > root.val:
                node = TreeNode(val)
                node.left = root
                return node
            
            root.right = dfs(root.right)
            return root
        
        return dfs(root)

# From discuss section

# Time: O(H)
# Space: O(1)

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        prev, curr = None, root
        while curr and curr.val > val:
            prev, curr = curr, curr.right
        
        node = TreeNode(val)
        node.left = curr
        if prev: # means prev is updated
            prev.right = node
            return root
        return node
            
        
        
        
        
