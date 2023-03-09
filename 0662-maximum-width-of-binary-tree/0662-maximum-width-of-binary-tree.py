# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        result = 0
        hash_map = defaultdict(lambda : [float("inf"), float("-inf")])
        
        def dfs(root, level, col):
            
            if not root:
                return
            
            hash_map[level][0] = min(hash_map[level][0], col)
            hash_map[level][1] = max(hash_map[level][1], col)
            
            dfs(root.left, level + 1, (col * 2) - 1)
            dfs(root.right, level + 1, (col * 2))
            
            return
        
        dfs(root, 0, 1)
        
        for row in hash_map:
            current = hash_map[row]
            result = max(result, current[-1] - current[0] + 1)
        
        return result
        
        
        
        
        
        
        
        
        
        
        