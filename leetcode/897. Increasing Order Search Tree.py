
# Link: https://leetcode.com/problems/increasing-order-search-tree/
#Q: 897. Increasing Order Search Tree

# Approach 1

# Time: O(N)
# Space: O(H + N)

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.root = head = TreeNode(1)
        def helper(root):
            nonlocal head
            if not root: return
            helper(root.left)
            head.right = TreeNode(root.val)
            head = head.right
            helper(root.right)
        
        helper(root)
        return self.root.right

# Approach 2

# Time: O(N)
# Space: O(H)

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = self.node = TreeNode(None)
        def helper(root):
            if not root: return
            helper(root.left)
            root.left = None
            self.node.right = root
            self.node = self.node.right
            helper(root.right)
        helper(root)
        return head.right
            


        
