
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#Q: 230. Kth Smallest Element in a BST

# Time: O(N)
# Space: O(N)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        inorder = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return inorder[k - 1]

# Time: O(K + H)
# Space: O(H)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
    
        
