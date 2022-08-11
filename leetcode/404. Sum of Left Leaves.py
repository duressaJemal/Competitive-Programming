# Link: https://leetcode.com/problems/sum-of-left-leaves/

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        
        def dfs(node, is_left_child):
            
            nonlocal total
            
            if not node: return
            if not node.left and not node.right:
                if is_left_child: total += node.val
            
            dfs(node.left, 1)
            dfs(node.right, 0)
            
        dfs(root, 0)
        return total

# BFS

# Time: O(N)
# Space: O(N)

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(root, 0)])
        total = 0
        
        while queue:
            
            node, is_left_child = queue.popleft()
            
            if not node.left and not node.right and is_left_child:
                total += node.val
            
            if node.left:
                queue.append((node.left, 1))
            if node.right:
                queue.append((node.right, 0))
                
        return total


