# Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
#Q: 700. Search in a Binary Search Tree

# Time: O(H)
# Space: O(H)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(root):
            if not root: return None
            if root.val == val: return root

            if root.val > val:
                return dfs(root.left)
            return dfs(root.right)
        
        return dfs(root)
        
# Time: O(N)
# Space: O(H)

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        self.output = None
        def dfs(root):
            
            if not root: return
            if root.val == val:
                self.output = root
            if root.val < val:
                dfs(root.right)
            else:
                dfs(root.left)
        
        dfs(root)
        return self.output


            
            
