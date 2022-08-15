# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# DFS

# Time: O(N)
# Space: O(H) -- where H = height

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        def dfs(node, max_value):
            
            nonlocal count
            if not node: return
        
            if node.val >= max_value:
                max_value = node.val
                count += 1
            
            dfs(node.left, max_value)
            dfs(node.right, max_value)
            
        dfs(root, float("-inf"))
        
        return count
