# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#Q: 105. Construct Binary Tree from Preorder and Inorder Traversal

# Time: O(N)
# Space: O(N)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.pre_index = 0
        
        def dfs(low, high):
            if low > high or self.pre_index == len(preorder):
                return None
            
            #Find the corresponding index in preorder
            index = inorder_index[preorder[self.pre_index]]
            node = TreeNode(inorder[index])
            self.pre_index += 1
            
            if low == high: return node
            
            node.left = dfs(low, index - 1)
            node.right = dfs(index + 1, high)
            return node
            
        # for accessing index from value
        inorder_index = {}
        for index, value in enumerate(inorder):
            inorder_index[value] = index
        
        return dfs(0, len(preorder) - 1)
