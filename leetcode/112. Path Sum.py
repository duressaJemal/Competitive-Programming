# link: https://leetcode.com/problems/path-sum/submissions/

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, SUM):
            
            SUM += node.val
            
            if not node.left and not node.right:
                
                return SUM == targetSum
            
            return (node.left and dfs(node.left, SUM)) or (node.right and dfs(node.right, SUM))
            
        return root and dfs(root, 0)
    


# BFS
    
# Time: O(N)
# Space: O(N)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root: 
            return False
        
        queue = deque([(root, targetSum)])
        
        while queue:
            
            node, SUM = queue.popleft()
            current_value = SUM - node.val
            
            if not node.left and not node.right and current_value == 0: 
                return True
            
            if node.left:
                queue.append((node.left, current_value))
            if node.right:
                queue.append((node.right, current_value))
            
        return False
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
