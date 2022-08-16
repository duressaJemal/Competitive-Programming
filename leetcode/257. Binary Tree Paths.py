# Link: https://leetcode.com/problems/binary-tree-paths/

# DFS 

# Time: O(N)
# Space: O(N))


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        output = []
        
        def dfs(node, path, output):
            
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    output.append(path)
                path += "->"
                dfs(node.left, path, output)
                dfs(node.right, path, output)
        
        dfs(root, "", output)
        
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
        
