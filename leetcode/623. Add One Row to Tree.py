
# Link: https://leetcode.com/problems/add-one-row-to-tree/
#Q: 623. Add One Row to Tree

# Time: O(N)
# Space: O(N)

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
    
        head = root
        queue = deque([root])
        level = 0
        while queue:
            n = len(queue)
            level += 1
            for _ in range(n):
                root = queue.popleft()
                if level + 1 == depth:
                    temp_l = root.left
                    temp_r = root.right
                    
                    left = TreeNode(val)
                    right = TreeNode(val)
                    
                    root.left = left
                    root.right = right
                    
                    left.left = temp_l
                    queue.append(left)
                    right.right = temp_r
                    queue.append(right)
                else:
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        return head
            
