
# Link: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
#Q: 1038. Binary Search Tree to Greater Sum Tree

# Approach - 1

# Time: O(N)
# Space: O(N)

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def traversal(root):
            if not root: return
            traversal(root.left)
            inorder_val.append(root.val)
            traversal(root.right)
        
        def transform(root):
            if not root: return
            transform(root.left)
            root.val = sufix[index[root.val]]
            transform(root.right)
            
        inorder_val = []
        traversal(root)
        
        n = len(inorder_val)
        index = {}
        for i in range(n):
            index[inorder_val[i]] = i
        
        # build sufix array
        sufix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            sufix[i] = sufix[i + 1] + inorder_val[i]
            
        transform(root)
        return root
        
# Approach - 2

# Time: O(N)
# Space: O(H)

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0
        def reversed_inorder(root):
            if not root: return
            reversed_inorder(root.right)
            self.total += root.val
            root.val = self.total
            reversed_inorder(root.left)
        
        reversed_inorder(root)
        return root
            
        
        
        
        
