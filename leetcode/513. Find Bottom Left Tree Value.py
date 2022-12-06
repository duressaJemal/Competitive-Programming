# Link: https://leetcode.com/problems/find-bottom-left-tree-value/
#Q: 513. Find Bottom Left Tree Value

# Time: O(N)
# Space: O(N)

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([root])
        left_most = root.val
        
        while queue:
            n = len(queue)
            left_most = queue[0].val
            for _ in range(n):
                root = queue.popleft()
                
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        
        return left_most
            
