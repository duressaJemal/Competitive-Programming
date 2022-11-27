
# Link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/
#Q: 429. N-ary Tree Level Order Traversal

# Time: O(N)
# Space: O(N)

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        output = []
        queue = deque([root]) if root else []
        while queue:
            n, store = len(queue), []
            for i in range(n):
                root = queue.popleft()
                store.append(root.val)
                for child in root.children:
                    queue.append(child)
            
            output.append(store)
        return output
                    
