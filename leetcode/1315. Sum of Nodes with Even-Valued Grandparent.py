# link: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# BFS

# time: O(n)
# space: O(n)

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        SUM = 0
        
        queue = deque([(root, False)])
        
        while queue:
            
            node, even_parent = queue.popleft()
            
            if even_parent:
                SUM += node.left.val if node.left else 0
                SUM += node.right.val if node.right else 0
            
            value = node.val % 2 == 0
            
            if node.left: 
                queue.append((node.left, value))
            if node.right: 
                queue.append((node.right, value))
               
        return SUM
    

# DFS

# time: O(n)
# space: O(n)

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        SUM = 0
        
        def dfs(node, even_parent):
            
            nonlocal SUM
            
            if not node:
                return 
            
            if even_parent:
                SUM += node.left.val if node.left else 0
                SUM += node.right.val if node.right else 0
            
            value = node.val % 2 == 0
            
            dfs(node.left, value)
            dfs(node.right, value)
            
        dfs(root, False)
        
        return SUM
        
        
