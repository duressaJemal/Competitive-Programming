# Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
#Q: 107. Binary Tree Level Order Traversal II

# Time: O(N)
# Space: O(N)

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []
        queue = deque([root]) if root else []
        while queue:
            n, store = len(queue), []
            for i in range(n):
                root = queue.popleft()
                store.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            
            output.append(store)
        return reversed(output)
            
