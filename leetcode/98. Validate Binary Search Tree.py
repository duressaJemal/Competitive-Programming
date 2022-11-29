
# Link: https://leetcode.com/problems/validate-binary-search-tree/
#Q: 98. Validate Binary Search Tree

# Time: O(N)
# Space: O(N)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        output = []
        
        def inorder(root):
            if not root: return
            inorder(root.left)
            output.append(root.val)
            inorder(root.right)
        
        inorder(root)
        i = 1
        mn = output[0]
        
        while i < len(output):
            if output[i] <= mn:
                return False
            mn = output[i]
            i += 1
        return True

# Time: O(N)
# Space: O(H)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.ans = True
        self.min = float("-inf")
        
        def helper(root):
            if not root: return
            helper(root.left)
            if root.val <= self.min:
                self.ans = False
            self.min = root.val
            helper(root.right)
        
        helper(root)
        return self.ans
        
        
