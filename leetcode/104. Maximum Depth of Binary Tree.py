# link: 

# time: O(n)
# space: O(n)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # DFS
        
        def dfs(root):
            
            if not root: return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            return max(left , right) + 1
        
        return dfs(root)


        # BFS
    
        dq = deque([root] if root else [])
        depth = 0
        
        while len(dq):
            
            length = len(dq)
            
            for _ in range(length):
                
                parent = dq.popleft()
                
                if parent.left:
                    dq.append(parent.left)
                if parent.right:
                    dq.append(parent.right)
                    
            depth += 1
            
        return depth
        
        
        
        
