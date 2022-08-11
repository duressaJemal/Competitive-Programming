# Link: https://leetcode.com/problems/leaf-similar-trees/

# DFS

# Time: O(N) -- where N = (size of tree1 + size of tree2)
# Space: O(N)

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        def dfs(node):

            if not node: return []
            container = []
            if not node.left and not node.right: 
                container += [node.val]
            container += dfs(node.left)
            container += dfs(node.right)
            
            return container
            
        output1 = dfs(root1)
        output2 = dfs(root2)
        
        return output1 == output2
            
