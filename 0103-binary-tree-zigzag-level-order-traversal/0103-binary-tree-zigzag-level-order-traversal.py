# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root] if root else [])
        flip = 0
        output = []
        
        while queue:
            
            temp = []
            for value in queue:
                temp.append(value.val) 
            
            if flip:
                output.append(temp[::-1])
                flip = 0
            else:
                output.append(temp)
                flip = 1
            
            n = len(queue)
            for _ in range(n):
                root = queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
             
        return output
                
            
            
            
        