
# Link: https://leetcode.com/problems/check-completeness-of-a-binary-tree/
#Q: 958. Check Completeness of a Binary Tree

# BFS(1)

# Time: O(N)
# Space: O(N)

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        index = 0
        queue = deque([(root, index)])
        level, not_filled_row = -1, False
        
        while queue:
            n = len(queue)
            level += 1
            if not_filled_row: return False

            if len(queue) < 2 ** level:
                prev = (2 ** level) - 2
                i = 0
                while i < len(queue):
                    if queue[i][1] - prev > 1:
                        return False
                    prev = queue[i][1]
                    i += 1
                not_filled_row = True
            
            for _ in range(n):
                root, index = queue.popleft()
                if root.left:
                    queue.append((root.left, 2 * index + 1))
                if root.right:
                    queue.append((root.right, 2 * index + 2))
            
        return True

# BFS(2)
    
# Time: O(N)
# Space: O(N)

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:              
                
                queue = deque([root])
                empty_node = False
                
                while queue:
                    n = len(queue)
                    for _ in range(n):
                        root = queue.popleft()
                        if not root:
                            empty_node = True
                            break
                        queue.append(root.left)
                        queue.append(root.right)
                    
                    if empty_node:
                        for i in range(len(queue)):
                            if queue[i]:
                                return False
                        return True
                return True
                    
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
        
    
