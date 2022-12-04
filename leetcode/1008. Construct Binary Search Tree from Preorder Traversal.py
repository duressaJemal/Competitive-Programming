
# Link: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
#Q: 1008. Construct Binary Search Tree from Preorder Traversal

# Time: O(N)
# Space: O(H)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        self.pre_index = 0
        def dfs(low, high):
            
            if self.pre_index >= len(preorder) or low > high: return None
            if low <= preorder[self.pre_index] <= high:
                node = TreeNode(preorder[self.pre_index])
                self.pre_index += 1
            else:
                return None
        
            node.left = dfs(low, node.val - 1)
            node.right = dfs(node.val + 1, high)
            
            return node
            
        return dfs(float("-inf"), float("inf"))
    
    
