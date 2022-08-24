# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# BFS

# Time: O(N)
# Space: O(N)

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root] if root else [])
        left_to_right = True
        output = []
        
        while queue:
            length = len(queue)
            temp = []
            
            for _ in range(length):
                parent = queue.popleft()
                temp.append(parent.val)
                if parent.left: queue.append(parent.left)
                if parent.right: queue.append(parent.right)
                    
            output.append(temp if left_to_right else temp[::-1])
            left_to_right = not left_to_right
               
        return output  
