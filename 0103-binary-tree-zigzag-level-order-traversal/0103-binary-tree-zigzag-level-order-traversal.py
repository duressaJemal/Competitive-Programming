# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(N)
# Space: O(N)

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root] if root else [])
        flip = False
        output = []
        
        while queue:
            
            temp = []
            n = len(queue)
            
            for _ in range(n):
                root = queue.popleft()
                temp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                
            if flip:
                output.append(temp[::-1])
            else:
                output.append(temp)
            
            flip = not flip
             
        return output
                
            
            
            
        