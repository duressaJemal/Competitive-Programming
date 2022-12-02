
# Link: https://leetcode.com/problems/recover-binary-search-tree/
#Q: 99. Recover Binary Search Tree

# Time: O(N)
# Space: O(N)

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        """
        Do not return anything, modify root in-place instead.
        """
        
        inorder = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            inorder.append(root)
            dfs(root.right)
            
        dfs(root)
        
        for i in range(len(inorder) - 1):
            if inorder[i].val > inorder[i + 1].val:
                start = i
                break
        
        for j in range(len(inorder) - 1, -1, -1):
            if inorder[j].val < inorder[j - 1].val:
                end = j
                break
        
        inorder[i].val, inorder[j].val = inorder[j].val, inorder[i].val
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
