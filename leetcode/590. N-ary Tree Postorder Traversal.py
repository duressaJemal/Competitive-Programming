# Link: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
#Q: 590. N-ary Tree Postorder Traversal

# DFS

# Time: O(N)
# Space: O(N)

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        output = []
        def dfs(root):
            if not root: return 
            for child in root.children:
                dfs(child)
            output.append(root.val)
            
        dfs(root)
        return output

# Iterative
    
# Time: O(N)
# Space: O(N)

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        output = []
        stack = [root] if root else []
        
        while stack:
            root = stack.pop()
            output.append(root.val)
            for child in root.children:
                stack.append(child)
            
        return output[::-1]
