# Link: https://leetcode.com/problems/binary-tree-paths/
#Q: 257. Binary Tree Paths

# Time: O(N)
# Space: O(N)

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        output = []
        
        def helper(root, path):
            if not root:
                return
      
            path += str(root.val)
            if not root.left and not root.right:
                output.append(path)
            
            if root.left:
                helper(root.left, path + "->")
            if root.right:
                helper(root.right, path + "->")
            
            
        helper(root, "")
        return output
    
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(node, path):
            
            if not node: 
                return []
            
            path += str(node.val)
            if not node.left and not node.right: 
                return [path]
            
            path += "->"
            return dfs(node.left, path) + dfs(node.right, path)
        
        return dfs(root, "")
        
