# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []
        
        hash_map = defaultdict(list)
        
        def dfs(root, row, col):
            
            if not root: return
            
            hash_map[col].append((row, root.val))
            
            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)
            
        
        dfs(root, 0, 0)
        
        columns = sorted(hash_map.keys())

        for column in columns:
            
            curr = hash_map[column]
            curr.sort()
            
            temp = [value for index, value in curr]
            output.append(temp)
        
        return output
            
            
            
            