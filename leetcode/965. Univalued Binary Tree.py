# Link: https://leetcode.com/problems/univalued-binary-tree/
#Q: 965. Univalued Binary Tree

# DFS(1)

# Time: O(N)
# Space: O(H)

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, value):
            
            if not node: return True
            if node.val != value: return False
            return dfs(node.left, value) and dfs(node.right, value)
        
        return dfs(root, root.val)
        

# DFS(2)

# Time: O(N)
# Space: O(H)

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, value):
            if not root: return True
            left = dfs(root.left, value)
            right = dfs(root.right, value)
            current = root.val == value
            return current and left and right
        
        return dfs(root, root.val)
