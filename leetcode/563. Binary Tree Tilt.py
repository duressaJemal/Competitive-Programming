#link: https://leetcode.com/problems/binary-tree-tilt/

# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        def dfs(root):
        
            nonlocal total
            if not root: return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            total += abs(left - right)
            
            return root.val + left + right
        
        dfs(root)
        return total
            

        
