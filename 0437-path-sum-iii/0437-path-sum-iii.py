# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(N)
# Space: O(N)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(root, total):
            if not root:
                return
            
            current_sum = total + root.val
            count[0] += hash_map[current_sum - targetSum]
            
            # add
            hash_map[current_sum] += 1
            
            dfs(root.left, current_sum)
            dfs(root.right, current_sum)
            
            # remove
            hash_map[current_sum] -= 1
            
        
        count = [0]
        hash_map = defaultdict(int)
        hash_map[0] = 1
        
        dfs(root, 0)
        return count[0]