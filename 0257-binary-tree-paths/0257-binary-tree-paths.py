# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Link: https://leetcode.com/problems/binary-tree-paths/
#Q: 257. Binary Tree Paths

# Time: O(N)
# Space: O(N)

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        output = []
        
        def helper(root, path):
            if not root:
                return
            
            path += str(root.val)
            if not root.left and not root.right:
                output.append(path)
                return
            
            if root.left:
                helper(root.left, path + "->")
            if root.right:
                helper(root.right, path + "->")
            
            
        helper(root, "")
        return output