# Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
#Q: 106. Construct Binary Tree from Inorder and Postorder Traversal

# Time: O(N)
# Space: O(N)

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        self.post_index = len(postorder) - 1
        
        def dfs(low, high):
            if low > high or self.post_index < 0: return None
            
            index = inorder_index_map[postorder[self.post_index]]
            node = TreeNode(inorder[index])
            self.post_index -= 1
            
            if low == high: return node
            
            node.right = dfs(index + 1, high)
            node.left = dfs(low, index - 1)
            return node
        
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index
        
        return dfs(0, len(postorder) - 1)
