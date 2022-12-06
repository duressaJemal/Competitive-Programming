# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#Q: 116. Populating Next Right Pointers in Each Node

# Time: O(N)
# Space: O(N)

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
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
                    
                    node.left.next = curr
                    curr = node.left
                    queue.append(node.left)
        return root

# From discuss section    

# Time: O(N)
# Space: O(H)

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def dfs(root):
            if not root: return None
            L, R, N = root.left, root.right, root.next
            if L:
                L.next = R
                if N:
                    R.next = N.left
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return root
        
        
        
        
