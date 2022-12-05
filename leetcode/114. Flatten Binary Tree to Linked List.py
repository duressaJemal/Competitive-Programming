# Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
#Q: 114. Flatten Binary Tree to Linked List


# Time: O(N)
# Space: O(H)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(root):
            if not root: return (None, None)
            
            left_node, left_end = dfs(root.left)
            right_node, right_end = dfs(root.right)
            
            if left_node and right_node:
                root.left = None
                root.right = left_node
                left_end.right = right_node
                return (root, right_end)
            
            if left_node:
                root.left = None
                root.right = left_node
                return (root, left_end)
            if right_node:
                root.right = right_node
                return (root, right_end)
            else:
                return (root, root)
                
        dfs(root)
    
# From discuss section

# Time: O(N)
# Space: O(H)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        self.prev = None
        
        def flatten(root):
            
            if not root: return None
            
            flatten(root.right)
            flatten(root.left)
            
            root.right = self.prev
            root.left = None
            self.prev = root
        
        flatten(root)
