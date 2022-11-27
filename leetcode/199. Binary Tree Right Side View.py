
# Link: https://leetcode.com/problems/binary-tree-right-side-view/
#Q: 199. Binary Tree Right Side View

# Time: O(N)
# Space: O(N)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        output = []
        queue = deque([root]) if root else []
        while queue:
            n = len(queue)
            output.append(queue[-1].val)
            for i in range(n):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            
        return output

# Time: O(N)
# Space: O(H)
                
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        output = []
        def helper(root, level):
            if not root: return
            if level == len(output):
                output.append(root.val)
            helper(root.right, level + 1)
            helper(root.left, level + 1)
            
        helper(root, 0)
        return output
            
