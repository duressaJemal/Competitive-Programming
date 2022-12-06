# Link: https://leetcode.com/problems/count-complete-tree-nodes/
#Q: 222. Count Complete Tree Nodes

# Time: O(log(N) ^ 2)
# Space: O(H)

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root: return 0
            
            left = 0
            node = root
            
            while node and node.left:
                node = node.left
                left += 1
            
            right = 0
            node = root
            
            while node and node.right:
                node = node.right
                right += 1
            
            if left == right:
                return 2 ** (left + 1) - 1
            else:
                return 1 + dfs(root.left) + dfs(root.right)
        
        return dfs(root)
