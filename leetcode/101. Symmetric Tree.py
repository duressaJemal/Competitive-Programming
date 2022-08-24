# Link: https://leetcode.com/problems/symmetric-tree/

# BFS

# Time: O(N)
# Space: O(N)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root.left and not root.right: return True
        
        queue = deque([]) # (node, is_left_subtree) 
        self.populate_queue(queue, root)
        
        while queue:
            
            length = len(queue)
            left, right = [], []
            
            for _ in range(length):
                parent, is_left = queue.popleft()
                
                if is_left:
                    left.append(parent.val if parent else None)
                else:
                    right.append(parent.val if parent else None)
                
                self.populate_queue(queue, parent)
            
            if left != right[::-1]:
                return False
        
        return True
                
    def populate_queue(self, queue, node):
        if not node: return
        queue.append((node.left, 1) if node.left else (None, 1))
        queue.append((node.right, 0) if node.right else (None, 0))
        
        

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
               
            if not root.left and not root.right:
                return root
            
            def dfs(left_node, right_node):
                
                # base case
                if not (left_node and right_node):
                    return left_node == right_node
                if left_node.val != right_node.val: return False
                return dfs(left_node.left, right_node.right) and dfs(left_node.right, right_node.left)
        
            return dfs(root.left, root.right)
