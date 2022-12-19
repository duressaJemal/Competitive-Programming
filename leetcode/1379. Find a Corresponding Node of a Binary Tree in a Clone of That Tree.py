# Link: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
#Q: 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

# Time: O(N)
# Space: O(H)

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(root):
            if not root: return None
            if root.val == target.val:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            return left or right
    
        return dfs(cloned)
