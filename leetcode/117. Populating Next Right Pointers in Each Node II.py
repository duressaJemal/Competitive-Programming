# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
#Q: 117. Populating Next Right Pointers in Each Node II


# Time: O(N)
# Space: O(N)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        queue = deque([root] if root else [])
        while queue:
            n = len(queue)
            curr = None
            for _ in range(n):
                node = queue.popleft()
                if node.right:
                    node.right.next = curr
                    curr = node.right
                    queue.append(node.right)
                
                if node.left:
                    node.left.next = curr
                    curr = node.left
                    queue.append(node.left)
                    
        return root
                    
        

        
        
        
        
        
        
        
        
        
        

                
