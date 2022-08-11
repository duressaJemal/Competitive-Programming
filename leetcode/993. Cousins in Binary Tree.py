# Link: https://leetcode.com/problems/cousins-in-binary-tree/

# BFS

# Time: O(N)
# Space: O(N)

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        queue = deque([(root, None)])
        container = []
        
        while queue:
            
            lenght = len(queue)
            for _ in range(lenght):
                
                node, parent = queue.popleft()
                
                if node.val == x or node.val == y:
                    container.append((node, parent))
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            
            if not container:
                continue
            
            if container and  len(container) == 2 and container[0][1] != container[1][1]:
                return True
            
            return False
            
        
