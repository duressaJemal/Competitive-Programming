# link: https://leetcode.com/problems/path-sum/submissions/

# DFS

# time: O(n)
# space: O(n)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        SUM = 0
        
        def dfs(node, SUM):
            
            SUM += node.val
            
            if not node.left and not node.right:
                return SUM == targetSum
            
            
            return (node.left and dfs(node.left, SUM)) or (node.right and dfs(node.right, SUM))
        
        return root and dfs(root, SUM)
     
        
# BFS

# time: O(n)
# space: O(n)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        
        queue = deque([(root, targetSum - root.val)])
        
        while queue:
            
            node, SUM = queue.popleft()
            
            if not node.left and not node.right and SUM == 0:
                return True
            
            if node.left:
                queue.append((node.left, SUM - node.left.val))
            if node.right:
                queue.append((node.right, SUM - node.right.val))
            
        return False
    



