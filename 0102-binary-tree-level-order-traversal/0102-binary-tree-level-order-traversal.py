# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root] if root else [])
        output = []
        
        while queue:
            
            n = len(queue)
            temp = []
            
            for _ in range(n):
                
                root = queue.popleft()
                temp.append(root.val)
                
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            
            output.append(temp)
        
        return output
                
            
                