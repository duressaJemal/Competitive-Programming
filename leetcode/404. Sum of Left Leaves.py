# Link: https://leetcode.com/problems/sum-of-left-leaves/

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.output = 0
        def helper(root):
            if not root: return
            if root.left:
                if not root.left.left and not root.left.right:
                    self.output += root.left.val
                helper(root.left)
            helper(root.right)
        helper(root)
        return self.output
    

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


